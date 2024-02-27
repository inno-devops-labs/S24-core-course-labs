variable "TIMEWEB_TOKEN" {
    type        = string
    description = "Timeweb API token. Put it in TF_VAR_TIMEWEB_TOKEN environment variable"
    sensitive = true
}

variable "server_name" {
  description = "Value of the name for the server"
  type        = string
  default     = "ExampleTimewebServer"
}
