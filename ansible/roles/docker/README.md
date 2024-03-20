## Docker Ansible Role
- Install docker and docker compose on ubuntu machines

## Requirements
- Ansible 3.10+
- Ubuntu OS

## Usage
```app_name: "app_python"
app_image_name: "staglente/app_python"
app_tag: "latest"

app_image: '{{ app_image_name }}:{{ app_tag }}'
app_path: "/app_python"

app_wipe: false
app_internal_port: 5000
app_external_port: 8000```