terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

resource "aws_instance" "app_server" {
  ami           = "ami-052c9ea013e6e3567"
  instance_type = "t2.micro"

  tags = {
    Name = var.instance_name
  }
}

provider "aws" {
  region = "us-west-2"
}
