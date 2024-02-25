resource "github_repository" "Devops-core-course-labs" {
  name               = "Devops-core-course-labs"
  description        = "This is a repository for the DevOps Core Course Labs"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "Python"
}

resource "github_branch_default" "main" {
  repository = github_repository.Devops-core-course-labs.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.Devops-core-course-labs.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
