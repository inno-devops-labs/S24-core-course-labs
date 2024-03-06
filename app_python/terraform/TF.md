## Tutorial following
### Output of the command "terraform state show"
```
Exactly one argument expected.
Usage: terraform [global options] state show [options] ADDRESS
  Shows the attributes of a resource in the Terraform state.

  This command shows the attributes of a single resource in the Terraform
  state. The address argument must be used to specify a single resource.
  You can view the list of available resources with "terraform state list".

Options:

  -state=statefile    Path to a Terraform state file to use to look
                      up Terraform-managed resources. By default it will
                      use the state "terraform.tfstate" if it exists.
```
### Output of the command "terraform state list"
```
docker_container.nginx
docker_image.nginx
```

### About applied changes
I add input input variable to tf file using following code:
```
variable "container_name" {
  description = "Value of the name for the Docker container"
  type        = string
  default     = "ExampleNginxContainer"
}
```
And when I change "name" parameter in "docker_container" section:
```
  name = var.container_name
```

finally, after applying changes the output of the command ```terraform apply``` was following:
```Apply complete! Resources: 1 added, 0 changed, 1 destroyed.```

### output of the commang "terraform output" 
Firstly, I used ```terraform destroy``` to stop container. After that I used ```terraform output``` command and get following output:
```
│ Warning: No outputs found
│
│ The state file either has no outputs defined, or all the defined outputs are empty. Please define an output in your configuration with the `output` keyword and run `terraform refresh` for it to become    
│ available. If you are using interpolation, please verify the interpolated value is not empty. You can use the `terraform console` command to assist.
```