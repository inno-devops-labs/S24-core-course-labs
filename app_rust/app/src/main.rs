use actix_web::{web, App, HttpServer};
use actix_web_prom::PrometheusMetricsBuilder;
use std::sync::Mutex;

pub mod service;
use crate::service::{handlers, state, visits};

pub mod tests;

const VISITS_STORAGE_FILE_PATH: &str = "app_data/visits";

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    println!("running on http://0.0.0.0:8000 (Press CTRL+C to quit)");

    let prometheus = PrometheusMetricsBuilder::new("actix")
        .endpoint("/metrics")
        .build()
        .unwrap();

    let state = web::Data::new(state::AppState {
        counter: Mutex::new(0),
        visits_storage: visits::VisitsFileStorage::new(String::from(VISITS_STORAGE_FILE_PATH)),
    });
    HttpServer::new(move || {
        App::new()
            .wrap(prometheus.clone())
            .app_data(state.clone())
            .service(handlers::base)
            .service(handlers::visits)
            .service(web::resource("/health").to(handlers::health))
    })
    .bind(("0.0.0.0", 8000))?
    .run()
    .await
}
