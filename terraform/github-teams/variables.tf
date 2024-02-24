variable "token" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}

variable "organization" {
  type        = string
  description = "Specifies the GitHub organization"
  sensitive   = true
  default = "fedor-ivn-devops-demo-org"
}

variable "repo" {
  type        = string
  description = "Repository name to bind the teams to"
  sensitive   = true
  default = "example-repo"
}
