//! src/main.rs
use learning_rust::configurations::*;
use learning_rust::startup::run;
use learning_rust::telemetry::{get_subscriber, initialize_subscriber};
use sqlx::postgres::PgPoolOptions;
use std::net::TcpListener;

#[tokio::main]
async fn main() -> std::io::Result<()> {
    let setting = get_configuration().expect("Failed to read the configurations");
    let subscriber = get_subscriber(
        "INFO",
        &setting.application.service_name,
        &setting.application.exporter_url,
    );
    initialize_subscriber(subscriber);
    let address = format!("{}:{}", setting.application.host, setting.application.port);
    let pool = PgPoolOptions::new().connect_lazy_with(setting.database.with_db());
    let listener = TcpListener::bind(address)?;
    run(listener, pool)?.await
}
