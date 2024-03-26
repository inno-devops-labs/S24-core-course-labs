# Metrics

## Log rotation

```yml
max-size: "20m"
max-file: "5"
```

## Memory limits

```yml
limits:
  memory: 200M
```

## healthcheck

```yml
healthcheck:
  test: [ "CMD", "curl", "-f", "http://localhost:8000" ]
  interval: 30s
  timeout: 15s
  retries: 3
```

## Screenshoots

### Prometheus targets
![img.png](./screenshoots/prom_metrics/app_python.png)
### Enchancements on Docker Compose configuration
![img.png](./screenshoots/prom_metrics/dashboard.png)
### Loki Dashboard
![img.png](./screenshoots/prom_metrics/loki.png)
### Prometheus Dashboard
![img.png](./screenshoots/prom_metrics/targets.png)

