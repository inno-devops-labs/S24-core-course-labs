variable "token" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}

variable "organization" {
  type        = string
  description = "Specifies the organization"
  sensitive   = true
  default     = "dzendos-org"
}

variable "repo" {
  type        = string
  description = "Repository name to bind the teams to"
  sensitive   = true
  default     = "sample-repo"
}