provider "aws" {
  region = var.aws_region
}

# Create a security group that allows SSH and HTTP traffic
resource "aws_security_group" "allow_ssh_http" {
  name        = "allow_ssh_http"
  description = "Allow SSH and HTTP inbound traffic"

  ingress {
    description = "SSH from ALL"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    description = "HTTP from ALL"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
}

resource "aws_instance" "server_python" {
  ami           = "ami-0faab6bdbac9486fb"
  instance_type = "t2.micro"
  key_name = aws_key_pair.deployer.key_name
  security_groups = [aws_security_group.allow_ssh_http.name]
  user_data = <<-EOF
              #!/bin/bash
              sudo apt update -y
              EOF

  tags = {
    Name = "server-python"
  }
}

resource "aws_instance" "server_bun" {
  ami           = "ami-0faab6bdbac9486fb"
  instance_type = "t2.micro"
  security_groups = [aws_security_group.allow_ssh_http.name]
  key_name = aws_key_pair.deployer.key_name
  user_data = <<-EOF
            #!/bin/bash
            sudo apt update -y
            EOF
  
  tags = {
    Name = "server-bun"
  }
}

resource "aws_key_pair" "deployer" {
  key_name   = "deployer"
  public_key = file("~/.ssh/id_rsa.pub")
}