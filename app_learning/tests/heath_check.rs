use reqwest::{Client, Response};
mod helpers;

#[tokio::test]
async fn test_health_check_endpoint() {
    let app = helpers::spawn_app().await;
    let client: Client = reqwest::Client::new();

    let response: Response = client
        .get(&format!("{}/health_check", &app.address))
        .send()
        .await
        .expect("Failed to make the request");

    assert_eq!(response.status(), 200)
}
