# Metrics

## Screenshots

### Prometheus Targets

![Alt text](screenshots/targets_1.png?raw=true)

![Alt text](screenshots/targets_2.png?raw=true)

### Dashboard for Loki

![Alt text](screenshots/dashboard_loki.png?raw=true)

### Dashboard for Prometheus

![Alt text](screenshots/dashboard_prometheus.png?raw=true)

## Service Configuration

### Log rotation mechanisms

Changes have been made to x-logging as outlined below:

```
x-logging: &default-logging
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "5"
    tag: "{{.ImageName}}|{{.Name}}"
```

In this configuration, the max-size parameter restricts the size of log files to 10 megabytes, while max-file sets a maximum of 5 log files. Docker automatically creates new files when limits are reached.

### Memory limits for containers

Added x-deploy to docker-compose.yml to cap service memory usage at 100MB:

```
x-deploy: &default-deploy
  resources:
    limits:
      memory: 100M
```
