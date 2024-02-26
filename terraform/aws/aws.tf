provider "aws" {
  region = var.region
}

resource "aws_instance" "app_server" {
  ami           = "ami-0cf1810907a781f00"
  instance_type = "t2.micro"
  tags = {
    Name = "app-server"
  }
}