variable "container" {
  description = "Name of container"
  type        = string
  default     = "devops-lab-task"
}

variable "image" {
  description = "Docker image"
  type        = string
  default     = "nytakoe115/flask-moscow-app"
}

variable "internal" {
  description = "Internal port"
  type        = number
  default     = 5000
}

variable "external" {
  description = "External port"
  type        = number
  default     = 8081
}