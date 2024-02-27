variable "tag_name" {
  description = "The name of the EC2 instance"
  type        = string
  default     = "example-instance"
}

variable "region" {
  description = "The AWS region to launch the instance"
  type        = string
  default     = "us-west-2"
}