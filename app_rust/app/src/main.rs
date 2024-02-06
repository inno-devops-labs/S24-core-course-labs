use std::sync::Mutex;
use actix_web::{web, App, HttpServer};

pub mod service;
use crate::service::{handlers, state};

pub mod tests;


#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let counter = web::Data::new(
        state::AppState {
            counter: Mutex::new(0),
        }
    );
    HttpServer::new(move ||{
        App::new()
            .app_data(counter.clone())
            .service(handlers::base)
    })
    .bind(("0.0.0.0", 8000)) ?
    .run()
    .await
}
