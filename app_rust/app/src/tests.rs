#[cfg(test)]
mod tests {
    use actix_web::{http::header::ContentType, test, web, App};
    use std::sync::Mutex;

    use crate::service::{handlers, state};

    #[actix_web::test]
    async fn test_get() {
        let counter = web::Data::new(state::AppState {
            counter: Mutex::new(0),
        });
        let app =
            test::init_service(App::new().app_data(counter.clone()).service(handlers::base)).await;
        let req = test::TestRequest::default()
            .insert_header(ContentType::plaintext())
            .to_request();

        let resp = test::call_service(&app, req).await;

        assert!(resp.status().is_success());
    }

    #[actix_web::test]
    async fn test_count() {
        let counter = web::Data::new(state::AppState {
            counter: Mutex::new(0),
        });
        let app =
            test::init_service(App::new().app_data(counter.clone()).service(handlers::base)).await;
        // first request to get request number == 1
        let req = test::TestRequest::default()
            .insert_header(ContentType::plaintext())
            .to_request();

        let resp = test::call_service(&app, req).await;

        assert_eq!(test::read_body(resp).await, "Request number: 1");

        // second request to check number updating
        let req = test::TestRequest::default()
            .insert_header(ContentType::plaintext())
            .to_request();

        let resp = test::call_service(&app, req).await;

        assert_eq!(test::read_body(resp).await, "Request number: 2");
    }
}
