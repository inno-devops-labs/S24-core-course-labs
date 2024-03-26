# Monitoring with Prometheus

## Prometheus Targets

![](imgs_for_report/targets.png)

## Loki Global Metrics Dashboard

![](imgs_for_report/loki_metrics.png)

## Prometheus Overview Dashboard

![](imgs_for_report/prometheus_overview.png)

## Log rotation and memory limits

The memory limits are specified for each container as follows:

```yaml
x-deploy:
  &default-deploy
  resources:
    limits:
      memory: 100m  <-- here
```

Log rotation is specified by max log file size:

```yaml
x-logging:
  &default-logging
  driver: "json-file"
  options:
    tag: "{{.ImageName}}|{{.Name}}"
    max-size: "10m"  <-- here
```