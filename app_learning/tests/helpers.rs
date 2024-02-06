use learning_rust::{
    configurations::{get_configuration, DatabaseSettings},
    startup::run,
    telemetry::{get_subscriber, initialize_subscriber},
};
use once_cell::sync::Lazy;
use sqlx::{postgres::PgPoolOptions, Executor, PgPool};
use std::net::TcpListener;

static TRACING: Lazy<()> = Lazy::new(|| {
    let setting = get_configuration().expect("Failed to read the configurations");
    let subscriber = get_subscriber("INFO", "test", &setting.application.exporter_url);
    initialize_subscriber(subscriber);
});

pub struct AppData {
    pub address: String,
    pub pool: PgPool,
}

pub async fn spawn_app() -> AppData {
    Lazy::force(&TRACING);
    let listener = TcpListener::bind("127.0.0.1:0").expect("Failed to create a listener");
    let port = listener.local_addr().unwrap().port();
    let mut configuration = get_configuration().expect("Could not read configurations");
    configuration.database.database_name = uuid::Uuid::new_v4().to_string();
    let pool = configure_database(&configuration.database).await;
    let server = run(listener, pool.clone()).expect("Could not create the server");
    let _ = tokio::spawn(server);
    let address = format!("http://127.0.0.1:{}", port);
    AppData {
        address: address,
        pool: pool,
    }
}

pub async fn configure_database(settings: &DatabaseSettings) -> PgPool {
    let db_server_url = settings.without_db();
    let pool = PgPoolOptions::new()
        .connect_with(db_server_url)
        .await
        .expect("Failed to connect to the database");
    pool.execute(&*format!(
        r#"CREATE DATABASE "{}";"#,
        settings.database_name
    ))
    .await
    .expect(&format!(
        "Failed to create the new database- name {}",
        settings.database_name
    ));

    let pool = PgPoolOptions::new()
        .connect_with(settings.with_db())
        .await
        .expect("Failed to connect to the database");
    sqlx::migrate!("./migrations/")
        .run(&pool)
        .await
        .expect("failed to run migrations");
    pool
}
