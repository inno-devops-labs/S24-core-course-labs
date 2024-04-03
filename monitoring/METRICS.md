# Metrics

## Successful setup of Prometheus
  ![prometheus](images/prometheus.png)

## Loki dashboard

  ![loki dashboard](images/loki_dashboard.png)

## Prometheus dashboard

  ![prometheus dashboard](images/prometheus_dashboard.png)

## Log rotation and limits

I've added limits to ensure log rotation: 

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

The promtail service can reach the metrics:

  ![app_python](images/metrics.png)

## Healthchecks

  ![healtchecks](images/healshchecks.png)