use crate::service::state::AppState;
use actix_web::{get, web, HttpResponse, Responder};
use serde::Serialize;

#[derive(Serialize)]
struct VisitsResponse {
    visits: u64,
}

impl VisitsResponse {
    fn new(_visits: u64) -> Self {
        Self { visits: _visits }
    }
}

#[get("/")]
pub async fn base(data: web::Data<AppState>) -> impl Responder {
    let mut counter = data.counter.lock().unwrap();
    *counter += 1;
    let _ = data.visits_storage.increment();

    HttpResponse::Ok().body(format!("Session request number: {}", counter))
}

#[get("/visits")]
pub async fn visits(data: web::Data<AppState>) -> impl Responder {
    let visits: u64 = data.visits_storage.read_data();

    HttpResponse::Ok().json(VisitsResponse::new(visits))
}

pub async fn health() -> HttpResponse {
    HttpResponse::Ok().finish()
}
