terraform {
   required_providers {
     github = {
       source  = "integrations/github"
       version = "~> 5.0"
     }
   }
 }

 provider "github" {
   token = var.token  
 }

resource "github_repository" "devops_repo" {
  name       = "test-lab"
  visibility = "public"
  has_issues = false
  has_wiki   = false
  auto_init  = false
}

resource "github_branch_protection" "main_protection" {
  repository_id                   = github_repository.devops_repo.id
  pattern                         = "main"
  require_conversation_resolution = true
  enforce_admins                  = true
}
