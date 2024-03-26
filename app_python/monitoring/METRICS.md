# Metrics

By following the guide (https://grafana.com/docs/grafana-cloud/quickstart/docker-compose-linux/) I managed to configure prometheus.

### Log rotation

```yaml
x-logging:
  &default-logging
  driver: "json-file"
  options:
    max-size: "5m"
    max-file: "3"
    tag: "{{.ImageName}}|{{.Name}}"

```

### Memory limit

```yaml
x-deploy:
  &default-deploy
  resources:
    limits:
      memory: 1000M
```

### Grafana
![](/S24-core-course-labs/app_python/monitoring/img/8.png)
### Targets
![](/S24-core-course-labs/app_python/monitoring/img/7.png)
