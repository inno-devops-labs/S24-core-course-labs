# Terraform

## Docker
Following the Docker tutorial from the Lab ReadMe file, I set up the Docker Infrastructure by following these two steps:  
1. Installing Terraform
2. Building the infrastructure.

The outputs were:  
1. ```terraform state list```
[Screenshot]
2. ```terraform state show```
[ScreenShot]
  

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
[Screenshot]

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
[Screenshot]
2. ```terraform state show```
[ScreenShot]
4. ```terraform output```
[Screenshot]

## Github

I followed the tutorial and deployed changes:
### Outputs
1. ```terraform state list```
[Screenshot]
2. ```terraform state show```
[ScreenShot]
4. ```terraform output```
[Screenshot]

After the above steps, I import the repository ```S24-core-course-labs``` and added branch protection to the main branch.

```bash
GITHUB_TOKEN=<redacted> terraform import "github_repository.S24-core-course-labs" "S24-core-course-labs"
```

Applying

```bash
GITHUB_TOKEN=<redacted> terraform apply
```
