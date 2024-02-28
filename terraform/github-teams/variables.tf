variable "token" {
  type        = string
  description = "Put here GitHub PAT token or GITHUB_TOKEN"
  sensitive   = true
}

variable "organization" {
  type        = string
  description = "Put here GitHub organization name"
  default = "timur-harin-devops"
  sensitive   = true
}

variable "repository" {
  type        = string
  description = "Put here GitHub repository name"
  default = "test-repo"
  sensitive   = true
}