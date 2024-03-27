# Metrics

## Table of Contents

- [Metrics](#metrics)
  - [Table of Contents](#table-of-contents)
  - [Configuration](#configuration)
  - [Dashboards](#dashboards)
  - [Log Rotation and Memory Limit](#log-rotation-and-memory-limit)
  - [Application Metrics](#application-metrics)
  - [Health Checks](#health-checks)

## Configuration

For this lab, I first modified my `docker-compose` to add prometheus to it. I also added a `prometheus.yml` file to configure prometheus to scrape metrics from both prometheus and loki containers. Along with those, `app_python`,`app_bun`, `grafana` and `promtail` containers were also scraped for metrics. This was visible in my prometheus dashboard at `http://localhost:9090/targets`.

![Prometheus Dashboard](https://i.postimg.cc/pLTJTKV6/image.png)

## Dashboards

After successful configuration of Loki and Prometheus dashboards, I could see the following-

![Graphana Prometheus](https://i.postimg.cc/Sj0LtPb2/image.png)

![Graphana Loki](https://i.postimg.cc/tgrMm9Ss/image.png)

## Log Rotation and Memory Limit

I used the following `docker-compose` configuration to all the containers to limit memory to 128MB and rotate logs after 500KB with 10 backups.

```yaml
x-logging: &default-logging
  driver: 'json-file'
  options:
    tag: '{{.ImageName}}|{{.ContainerName}}'
    max-size: '500k'
    max-file: '10'

x-deploy: &default-deploy
  resources:
    limits:
      memory: 128M
```

## Application Metrics

To collect application metrics properly, I had to configure the `app_python` and `app_bun` containers so that they could collect the metrics for prometheus. For the python application `flask-prometheus-exporter` was used while for the bun application it was `prom-client`. The metrics were exposed to `/metrics` endpoints for each. To test, I automated some requests to the `/` endpoint and checked the metrics using prometheus.

![App Metrics](https://i.postimg.cc/QtsbjwFp/image.png)

## Health Checks

I implemented health checks for all the containers in the `docker-compose` file. The health checks were implemented using the `curl` command to check the healthcheck endpoints of each container (except for `promtail` container).
