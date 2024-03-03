terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "eu-north-1"
}

variable "private_key_path" {
  description = "The path to the private key"
  default     = "~/.ssh/aws"
}

variable "public_key_path" {
  description = "The path to the public key"
  default     = "~/.ssh/aws.pub"
}

locals {
  private_key = file(var.private_key_path)
  public_key = file(var.public_key_path)
}

resource "aws_key_pair" "key" {
  key_name   = "aws"
  public_key = local.public_key
}

resource "aws_instance" "app_server" {
  ami           = "ami-00381a880aa48c6c6"
  instance_type = "t3.micro"
  key_name = aws_key_pair.key.key_name

  connection {
    type        = "ssh"
    user        = "ec2-user" # Default user for Amazon Linux 2 instances
    private_key = local.private_key
  }

  vpc_security_group_ids = [aws_security_group.sg_ec2.id]

  tags = {
    Name = "DevOps-S24"
  }
}