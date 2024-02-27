variable "team_name_1" {
  type        = string
  description = "some team"
  default     = "some-team"
}

variable "team_description_1" {
  type        = string
  description = "some team description"
  default     = "cool team"
}

variable "team_name_2" {
  type        = string
  description = "some other team"
  default     = "some-other-team"
}

variable "team_description_2" {
  type        = string
  description = "some other team description"
  default     = "cooler team"
}

variable "token" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}


variable "organization" {
  type        = string
  description = "github organization"
  sensitive   = true
  default     = "probirochniy-devops-test-org"
}

variable "github_repository" {
  type        = string
  description = "github repo"
  default     = "devops-example"
}
