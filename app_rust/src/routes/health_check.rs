use actix_web::{HttpResponse, Responder};
use prometheus::{Encoder, TextEncoder};

pub async fn health_check() -> impl Responder {
    HttpResponse::Ok().finish()
}

pub async fn metric() -> impl Responder {
    let encoder = TextEncoder::new();
    let metric_families = prometheus::gather();
    let mut buffer = vec![];
    if let Err(e) = encoder.encode(&metric_families, &mut buffer) {
        return HttpResponse::InternalServerError().body(format!("Cannot encode metrics: {}", e));
    }
    HttpResponse::Ok()
        .content_type(encoder.format_type())
        .body(buffer)
}
