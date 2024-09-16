variable "provider_socket" {
  type        = string
  description = "Socket for docker daemon"
}

variable "container_name" {
  type        = string
  description = "Name for app_go container"
  default     = "app_go"
}

variable "container_pg_name" {
  type        = string
  description = "Name for pg container"
  default     = "pg"
}

variable "external_port" {
  type        = number
  description = "Port for container to forward"
  default     = 8079
}

variable "external_pg_port" {
  type        = number
  description = "Port for container pg to forward"
  default     = 5432
}

variable "PG_USER" {
  type      = string
  sensitive = true
}

variable "PG_PASSWORD" {
  type      = string
  sensitive = true
}

variable "PG_DBNAME" {
  type      = string
  sensitive = true
}

variable "ENV" {
  type    = string
  default = "local" # testing, production todo
}

variable "SERVER_HOST" {
  type    = string
  default = "0.0.0.0"
}

variable "DB_HOST" {
  type    = string
  default = "172.6.0.10"
}

variable "SERVER_PORT" {
  type    = number
  default = 8080
}