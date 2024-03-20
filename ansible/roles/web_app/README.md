# Web App Role
role that deploys web app

## Requirements
- Ubuntu
- Ansible
- Python
- Docker role

## Usage
```app_name: "app_python"
app_image_name: "staglente/app_python"
app_tag: "latest"

app_image: '{{ app_image_name }}:{{ app_tag }}'
app_path: "/app_python"

app_wipe: false
app_internal_port: 5000
app_external_port: 8000```