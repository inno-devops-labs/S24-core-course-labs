### Variables.tf ###

variable "token" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
  default     = "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"
}