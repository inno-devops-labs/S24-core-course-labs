mod helpers;
use learning_rust::routes::{CreateSubjectRequest, CreateSubjectResponse};
use uuid::Uuid;

#[tokio::test]
async fn test_subject_creation_200() {
    let app = helpers::spawn_app().await;
    let client = reqwest::Client::new();
    let body = CreateSubjectRequest {
        name: "test_name".to_string(),
    };
    let response = client
        .post(&format!("{}/subject", &app.address))
        .json(&body)
        .send()
        .await
        .expect("Failed to make this request");
    assert!(
        response.status().is_success(),
        "Expected 200 but found {}",
        response.status().as_str()
    );
    let val = response
        .json::<CreateSubjectResponse>()
        .await
        .expect("Could not parse the response");
    assert_ne!(val.id, Uuid::nil());
    assert!(!val.thread_id.is_empty());
    assert!(!val.assistant_id.is_empty());
    assert!(!val.name.is_empty());

    let saved = sqlx::query!(r#"SELECT id, name FROM subjects"#)
        .fetch_one(&app.pool)
        .await
        .expect("Failed to get subject just created");

    assert_eq!(saved.id, val.id);
    assert_eq!(saved.name.unwrap(), val.name);
}

#[tokio::test]
async fn test_subject_creation_400() {
    let test_cases = vec![(
        CreateSubjectRequest {
            name: String::new(),
        },
        "the name cannot be empty",
    )];
    let app = helpers::spawn_app().await;
    let client = reqwest::Client::new();
    for (invalid_body, error) in test_cases {
        let response = client
            .post(&format!("{}/subject", &app.address))
            .json(&invalid_body)
            .send()
            .await
            .expect("Failed to make this request");
        assert_eq!(
            response.status().as_u16(),
            400,
            "Test failed - the expected error is {}",
            error
        );
    }
}
