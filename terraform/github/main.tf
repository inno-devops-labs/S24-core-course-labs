resource "github_repository" "devops" {
  name = "S24-core-course-labs"
  visibility = "public"
}

resource "github_branch_default" "main" {
  repository = github_repository.devops.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.devops.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}