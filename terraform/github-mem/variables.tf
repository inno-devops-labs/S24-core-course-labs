variable "token" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}

variable "organization" {
  type        = string
  description = "Specifies the GitHub organization"
  sensitive   = true
  default = "Test-Teraform"
}

variable "repo" {
  type        = string
  description = "Repository name"
  sensitive   = true
  default = "Testing-team"
}