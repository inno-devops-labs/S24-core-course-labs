use actix_web::dev::Server;
use actix_web::{web, App, HttpServer};
use sqlx::PgPool;
use std::net::TcpListener;
use tracing_actix_web::TracingLogger;

use crate::routes::{health_check, metric, subject};

pub fn run(listener: TcpListener, pool: PgPool) -> Result<Server, std::io::Error> {
    let db_pool = web::Data::new(pool);
    let server = HttpServer::new({
        move || {
            App::new()
                .wrap(TracingLogger::default())
                .app_data(db_pool.clone())
                .route("health_check", web::get().to(health_check))
                .route("/subject", web::post().to(subject))
                .route("/metrics", web::get().to(metric))
        }
    })
    .listen(listener)?
    .run();

    Ok(server)
}
