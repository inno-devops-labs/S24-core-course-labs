use actix_web::{web, get, HttpResponse, Responder};
use crate::service::state::AppState;


#[get("/")]
pub async fn base(data: web::Data<AppState>) -> impl Responder {
    let mut counter = data.counter.lock().unwrap();
    *counter += 1;

    HttpResponse::Ok().body(format!("Request number: {}", counter))
}
