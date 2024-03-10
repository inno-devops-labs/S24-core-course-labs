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
  region = "us-east-1" # Placeholder region for MinIO compatibility
  # defined in env. But service is only available in vpn, good luck to crack
  #   access_key = "pOHzZLHnJNIyL30lF9fv"
  #   secret_key = "Am1sIdGOCVhujIcuIhKggd9FDHtMZejAD6SltGui"
  endpoints {
    s3 = "http://mqmini:19000" # server in vpn network with minio. Check the docker-compose.yml
  }
  skip_credentials_validation = true
  skip_requesting_account_id  = true
  s3_use_path_style           = true
}

resource "aws_s3_bucket" "minio_bucket" {
  bucket = "myterraformbucket1"

  tags = {
    Name = "My Terraform Bucket"
  }
}

resource "aws_s3_object" "hello_world_object" {
  bucket  = aws_s3_bucket.minio_bucket.id
  key     = "hello.txt"
  content = "Hello, world!"

  tags = {
    Name = "Hello World Object"
  }
}
