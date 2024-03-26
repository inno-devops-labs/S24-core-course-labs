# Metrics 

## Prometheus 
Developed a `prometheus.yml` configuration file to enable the scraping of metrics from Loki and Prometheus containers at 10-second intervals, alongside updating the `docker-compose.yml` file to incorporate Prometheus as a service, and subsequently integrated the Prometheus client into both the `app_python` and `app_rust` applications, facilitating metric retrieval via the `/metrics` endpoint.


### `Screenshot ot the Targets`
[![image.png](https://i.postimg.cc/43qgkJLF/image.png)](https://postimg.cc/jWH9yrrz)


## Dashboards
### Dashboards
### Dashboard (Loki)
[![image.png](https://i.postimg.cc/JnmwXWZg/image.png)](https://postimg.cc/gwMB9QMq)
### Dashboard (Prometheus)
[![image.png](https://i.postimg.cc/jq8hsLQ5/image.png)](https://postimg.cc/t7x6kRcQ)

## Log rotation
In the `docker-compose.yml` file, I included log rotation and memory limits for all services, setting containers to have a memory limit of 200MB and implementing log rotation to maintain 10 files, each capped at 10MB in size.
```bash
x-deploy: &default-deploy
  resources:
    limits:
      memory: 200M

x-logging:
  &common_logging
  driver: "json-file"
  options:
    tag: "{{.ImageName}}|{{.ContainerName}}"
    max-size: "10M"
    max-file: "10"
```
## Application Metrics 
### app_python
[![image.png](https://i.postimg.cc/ryd9wqhN/image.png)](https://postimg.cc/Sjh9Zbbn)

