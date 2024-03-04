terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.2.0"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = var.region
}