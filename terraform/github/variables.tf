variable "token" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}

variable "name" {
  description = "Devops test repo"
  type        = string
  default     = "terraform-lab-4"
}

variable "description" {
  description = "Test repo description"
  type        = string
  default     = "Terraform default description"
}

variable "organization" {
  type    = string
  default = "devops-terraform-lab4"
}

variable "team1" {
  description = "Team 1"
  type        = string
  default     = "First team"
}

variable "team2" {
  description = "Team 2"
  type        = string
  default     = "Second team"
}