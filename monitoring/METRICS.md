# Metrics

## Successful setup of Prometheus
  ![prometheus](screens/prometheus.png)

## Log rotation and limits

Limits for log rotation: 

```yaml
x-logging:
  &default-logging
  driver: "json-file"
  options:
    max-size: 200k
    max-file: 10
    tag: "{{.ImageName}}|{{.Name}}"

x-deploy:
  &default-deploy
  resources:
    limits:
      memory: 100M
```

## Application metrics

Metrics:

  ![app_python](screens/metrics.png)

## Healthchecks

  ![healtchecks](screens/health.png)