variable "server_name" {
  description = "Name for the server"
  type        = string
  default     = "Default server name"
}

variable "twc_token" {
  type        = string
  description = "Specifies the TimeWeb API token"
  sensitive   = true
}
