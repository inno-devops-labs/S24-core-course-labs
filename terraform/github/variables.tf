variable "token" {
  type        = string
  description = "Put here GitHub PAT token or GITHUB_TOKEN"
  sensitive   = true
}

variable "user" {
  type        = string
  description = "Put here GitHub user name"
  sensitive   = true
}