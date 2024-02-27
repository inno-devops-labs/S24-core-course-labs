# Terraform

## Docker
Following the Docker tutorial from the Lab ReadMe file, I set up the Docker Infrastructure by following these two steps:  
1. Installing Terraform
2. Building the infrastructure.

The outputs were:  
1. ```terraform state list```
![State List of Docker](https://raw.githubusercontent.com/tanmaysharma2001/S24-core-course-labs/lab04/images/lab%204/Terraform%20State%20Show.png)
2. ```terraform state show docker_container.app_python```
![Docker Container State](https://raw.githubusercontent.com/tanmaysharma2001/S24-core-course-labs/lab04/images/lab%204/Terraform%20State%20List.png)
![Docker Container State 2](https://raw.githubusercontent.com/tanmaysharma2001/S24-core-course-labs/lab04/images/lab%204/Terraform%20State%20List%202.png)
  

Utilized input variables to rename the Docker container:  
```terraform
variable "container_name" {
  description = "Container's name"
  type        = string
  default     = "application-weather"
}

variable "container_image" {
  description = "Image name"
  type        = string
  default     = "sharmatanmay617/devops-lab-2:latest"
}

variable "int_port" {
  description = "Internal Port"
  type        = number
  default     = 5000
}

variable "ext_port" {
  description = "External port"
  type        = number
  default     = 5000
}
```

4. ```terraform output```
![Terraform Ouptut](https://raw.githubusercontent.com/tanmaysharma2001/S24-core-course-labs/lab04/images/lab%204/Terraform%20Output.png)

## AWS

Before starting with the AWS building I first generated an Access Token by creating an IAM account.  

### Building

Initliasing

```bash
AWS_ACCESS_KEY_ID=<redacted> AWS_SECRET_ACCESS_KEY=<redacted> terraform init
```

Formatting and Validating

```bash
terraform fmt
terraform validate
```

Applying

```bash
AWS_ACCESS_KEY_ID=<redacted> AWS_SECRET_ACCESS_KEY=<redacted> terraform apply
```

### Outputs
1. ```terraform state list```
![State List](https://raw.githubusercontent.com/tanmaysharma2001/S24-core-course-labs/lab04/images/lab%204/aws/Terraform%20state%20list.png)
2. ```terraform state show```
![State Show](https://raw.githubusercontent.com/tanmaysharma2001/S24-core-course-labs/lab04/images/lab%204/aws/Terraform%20State%20Show%201.png)
![State Show 2](https://raw.githubusercontent.com/tanmaysharma2001/S24-core-course-labs/lab04/images/lab%204/aws/Terraform%20State%20Show%202.png)
![State Show 3](https://raw.githubusercontent.com/tanmaysharma2001/S24-core-course-labs/lab04/images/lab%204/aws/Terraform%20State%20Show%203.png)
4. ```terraform output```
![Terraform Output](https://raw.githubusercontent.com/tanmaysharma2001/S24-core-course-labs/lab04/images/lab%204/aws/Terraform%20Output.png)

## Github

I followed the tutorial and deployed changes:
### Applying
![Applying Deploy Plan](https://raw.githubusercontent.com/tanmaysharma2001/S24-core-course-labs/lab04/images/lab%204/github/Terraform%20Apply%20Deploy%20Plan.png)

After the above steps, I import the repository ```S24-core-course-labs``` and added branch protection to the main branch.

```bash
GITHUB_TOKEN=<redacted> terraform import "github_repository.S24-core-course-labs" "S24-core-course-labs"
```

Applying

```bash
GITHUB_TOKEN=<redacted> terraform apply
```

![Apply](https://raw.githubusercontent.com/tanmaysharma2001/S24-core-course-labs/lab04/images/lab%204/github/Terraform%20Apply.png)
