variable "GITHUB_TOKEN" {
  description = "GitHub PAT token (should be put in TF_VAR_GITHUB_TOKEN)"
  type        = string
  sensitive   = true
}

variable "repository_name" {
    description = "GitHub repository name"
    type = string
    default = "S24-core-course-labs"
}

variable "repository_description" {
    description = "GitHub repository description"
    type = string
    default = "Innopolis University DevOps course labs solutions."
}

variable "organization_name" {
    description = "GitHub organization name"
    type = string
    default = "Test-devops-organization"
}
