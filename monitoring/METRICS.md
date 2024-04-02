# Metrics for Python Application

## System setup

![Successful Docker Compose run](./screenshots/compose_with_prometheus.png)

## Prometheus targets

![Prometheus targets](./screenshots/prometheus_targets.png)

## Grafana dashboards

### Loki

![Loki Dashboard](./screenshots/loki_dashboard.png)

### Prometheus

![Prometheus Dashboard](./screenshots/prometheus_dashboard.png)

## Container & Logging configuration

Every service is configured with the following settings:

```yaml
deploy:
  resources:
    limits:
      memory: 500M
logging:
  driver: "json-file"
  options:
    max-size: "200k"
    max-file: "10"
    tag: "{{.ImageName}}|{{.Name}}"
```

Every container is limited to 200M memory and uses JSON files as logging option. Log rotation consists of 10 last files each at most 200k in size.
