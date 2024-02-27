variable "token" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}

variable "name" {
  type    = string
  default = "devops-demo-repo"
}

variable "org" {
  type    = string
  default = "dev0ps-demo-org"
}
