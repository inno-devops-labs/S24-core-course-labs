resource "github_repository" "S24-core-course-labs" {
  name               = "S24-core-course-labs"
  description        = "Repo with the solutions to S24-DevOps course in Innopolis University"
  visibility         = "public"
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "Python"
}


resource "github_branch_default" "main" {
  repository = github_repository.S24-core-course-labs.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id = github_repository.S24-core-course-labs.id
  pattern       = github_branch_default.main.branch
}