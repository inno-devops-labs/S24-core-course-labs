variable "token" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}

variable "owner" {
  type        = string
  description = "Specifies the GitHub owner"
  default     = "example-org-123"
}
