# Custom role to deploy web app Docker image

## Requirements

1. Ubuntu host
2. Python
3. docker role

## Usage

```yaml
- roles:
    - role: web_app
      image_name: "some_name"
      image_tag: "some_tag"
      ports:
        - 8080:8080
      wipe: false
```