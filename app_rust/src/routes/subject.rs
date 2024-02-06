use actix_web::{
    web::{self},
    HttpResponse, Responder,
};
use chrono::Utc;
use sqlx::PgPool;

#[derive(serde::Deserialize, serde::Serialize, Debug)]
pub struct CreateSubjectRequest {
    pub name: String,
}

#[derive(serde::Deserialize, serde::Serialize, Debug)]
pub struct CreateSubjectResponse {
    pub id: uuid::Uuid,
    pub assistant_id: String,
    pub name: String,
    pub thread_id: Vec<String>,
    pub owner: uuid::Uuid,
    pub created_at: chrono::DateTime<Utc>,
}

#[tracing::instrument(
    name = "Adding a new subject", skip(data, pool),
    fields(
    subject_name = data.name
    ))]
pub async fn subject(
    data: web::Json<CreateSubjectRequest>,
    pool: web::Data<PgPool>,
) -> impl Responder {
    tracing::info!("Creating a new subject");
    if data.name.is_empty() {
        tracing::error!(
            "Failed to complete the request, the name of the subject was  not provided"
        );
        HttpResponse::BadRequest().finish()
    } else {
        match insert_subject(&data, &pool).await {
            Ok(resp) => {
                tracing::info!("Succesfully inserted into the database");
                HttpResponse::Ok().json(resp)
            }
            Err(e) => {
                tracing::error!("Database insetion failed with error {}", e);
                HttpResponse::InternalServerError().finish()
            }
        }
    }
}

#[tracing::instrument(
    name = "Saving new subscriber details in the database",
    skip(req, pool)
)]
pub async fn insert_subject(
    req: &CreateSubjectRequest,
    pool: &PgPool,
) -> Result<CreateSubjectResponse, sqlx::Error> {
    let resp = CreateSubjectResponse {
        id: uuid::Uuid::new_v4(),
        assistant_id: "assis-45632".to_string(),
        owner: uuid::Uuid::new_v4(),
        thread_id: vec!["thread-12345".to_string(), "thread-54732".to_string()],
        name: req.name.clone(),
        created_at: chrono::Utc::now(),
    };

    sqlx::query!(
        r#"INSERT INTO subjects (id, name, assistant_id, owner, created_at) VALUES ($1, $2, $3, $4, $5) RETURNING id"#,
        resp.id ,resp.name, resp.assistant_id, resp.owner, resp.created_at)
        .fetch_one(pool)
        .await?;
    Ok(resp)
}
