resource "github_repository" "test-devops-terraform-repo" {
  name             = "test-devops-terraform-repo"
  description      = "Test terraform for devops lab"
  visibility       = "public"
  has_issues       = true
  has_wiki         = true
  auto_init        = true
  license_template = "mit"
}


resource "github_branch_default" "main" {
  repository = github_repository.test-devops-terraform-repo.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.test-devops-terraform-repo.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
