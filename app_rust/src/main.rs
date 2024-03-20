//! This crate provides a simple Actix web server that exposes an endpoint for
//! getting the current time in Moscow. It also integrates with the
//! `actix-web-prom` crate to expose Prometheus metrics.
//!
//! For more information, see the
//! [README.md](https://github.com/yourusername/yourrepository/README.md) file.
#![warn(
    clippy::all,
    clippy::style,
    clippy::pedantic,
    clippy::missing_docs_in_private_items,
    clippy::dbg_macro,
    clippy::else_if_without_else,
    clippy::get_unwrap,
    clippy::if_then_some_else_none,
    clippy::todo,
    clippy::min_ident_chars,
    clippy::similar_names
)]

use actix_web::{get, web, App, HttpResponse, HttpServer, Responder};
use actix_web_prom::PrometheusMetricsBuilder;
use chrono::{DateTime, Utc};
use chrono_tz::{Europe::Moscow, Tz};
use serde::{Serialize, Serializer};

/// Response struct for the current time in Moscow.
#[derive(Serialize)]
struct CurrentTimeResp {
    /// Current time in Moscow.
    #[serde(serialize_with = "serialize_datetime")]
    current_time: DateTime<Tz>,
}

impl CurrentTimeResp {
    /// Create current time response.
    fn new() -> Self {
        Self {
            current_time: Utc::now().with_timezone(&Moscow),
        }
    }
}

/// Serialize Time-zoned datetime to string.
fn serialize_datetime<S: Serializer>(
    datetime: &DateTime<Tz>,
    serializer: S,
) -> Result<S::Ok, S::Error> {
    let datetime = format!("{}", datetime.format("%Y-%m-%d %H:%M:%S"));
    serializer.serialize_str(&datetime)
}

/// Route for getting the current time in Moscow.
#[get("/")]
async fn moscow_time() -> impl Responder {
    println!("Received request for Moscow time");
    HttpResponse::Ok().json(CurrentTimeResp::new())
}

/// Route for health check.
async fn health() -> HttpResponse {
    HttpResponse::Ok().finish()
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    println!("Starting server at port {}", 80);

    let prometheus = PrometheusMetricsBuilder::new("actix")
        .endpoint("/metrics")
        .build()
        .unwrap();

    HttpServer::new(move || {
        App::new()
            .wrap(prometheus.clone())
            .service(moscow_time)
            .service(web::resource("/health").to(health))
    })
    .bind(("0.0.0.0", 80))?
    .run()
    .await
}

#[cfg(test)]
mod tests {
    use actix_web::{http::header::ContentType, test, App};

    use super::*;

    #[actix_web::test]
    async fn test_get_returns_success() {
        let app = test::init_service(App::new().service(moscow_time)).await;
        let req = test::TestRequest::default()
            .insert_header(ContentType::plaintext())
            .to_request();

        let resp = test::call_service(&app, req).await;
        assert!(resp.status().is_success());
    }

    #[actix_web::test]
    async fn test_time_is_equal() {
        let app = test::init_service(App::new().service(moscow_time)).await;
        let req = test::TestRequest::default()
            .insert_header(ContentType::plaintext())
            .to_request();
        let resp = test::call_and_read_body(&app, req).await;
        let resp = String::from_utf8(resp.to_vec()).unwrap();
        let actual = serde_json::to_string(&CurrentTimeResp::new()).unwrap();
        assert_eq!(resp, actual);
    }
}
