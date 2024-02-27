resource "github_repository" "DevOps-Engineering-Labs" {
  name               = "DevOps-Engineering-Labs"
  description        = "DevOps lab"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  license_template   = "mit"
}


resource "github_branch_default" "main" {
  repository = github_repository.DevOps-Engineering-Labs.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.DevOps-Engineering-Labs.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}