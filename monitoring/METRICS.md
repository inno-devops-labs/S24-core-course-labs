# Metrics

## Prometheus targets

![Prometheus targets](./screenshots/prometheus_targets.png)

## Loki dashboard

![Loki dashboard](./screenshots/loki_dashboard.png)

## Prometheus dashboard

![Prometheus dashboard](./screenshots/prometheus_dashboard.png)

## Service Configuration Updates

### Log rotation

For log rotation mechanisms I added `max-size` and `max-file` parameters. So docker can keep up to 3 log files for each service, each log file - maximum of 50MB.
```sh
x-logging:
  &default-logging
  driver: "json-file"
  options:
    max-size: "50m"
    max-file: "3"
    tag: "{{.ImageName}}|{{.Name}}"
```

### Memory limits

Memory limit is a maximum of 128MB.
```sh
x-deploy:
  &default-deploy
  resources:
    limits:
      memory: 128M
```

And I updated the configurations of all services with `deploy: *default-deploy` to use this memory limits.

## Metrics and Health Checks