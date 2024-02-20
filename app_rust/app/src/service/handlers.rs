use crate::service::state::AppState;
use actix_web::{get, web, HttpResponse, Responder};

#[get("/")]
pub async fn base(data: web::Data<AppState>) -> impl Responder {
    let mut counter = data.counter.lock().unwrap();
    *counter += 1;

    HttpResponse::Ok().body(format!("Request number: {}", counter))
}
