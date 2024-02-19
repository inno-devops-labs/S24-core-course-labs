variable "token" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}

provider "github"{
    token=var.token
    owner="RamPrinOrg"	
}

terraform {
  required_version = "~> 1.0"

  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

module "team" {
 source  = "mineiros-io/team/github"
 version = "~> 0.8.0"

  name        = "Engineering"
  description = "This team is created with terraform to test the terraformn-github-repository module."
  privacy     = "closed"

  members     = ["RamPrin", "teexone"]
  maintainers = ["RamPrin"]

  pull_repositories = [
    github_repository.repo.name,
  ]
  push_repositories = [
    github_repository.DevOps.name,
  ]
}

resource "github_repository" "repo" {
  name               = "Terraform-S24"
}

resource "github_repository" "DevOps" {
  name             = "DevOps"
}

