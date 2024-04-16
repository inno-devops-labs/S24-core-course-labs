# Prometheus

Successful scrape from all targets in `docker-compose.yml`:

![Screenshot from 2024-03-27 00-47-05.png](img%2FScreenshot%20from%202024-03-27%2000-47-05.png)

# Grafana

Prometheus dashboard in grafana:

![Screenshot from 2024-03-27 00-50-17.png](img%2FScreenshot%20from%202024-03-27%2000-50-17.png)

Loki dashboard in grafana:

![Screenshot from 2024-03-27 00-51-34.png](img%2FScreenshot%20from%202024-03-27%2000-51-34.png)

Web app python metrics in grafana using prometheus:

![Screenshot from 2024-03-27 01-10-23.png](img%2FScreenshot%20from%202024-03-27%2001-10-23.png)

Web app java
metrics in grafana using prometheus:

![Screenshot from 2024-03-27 01-10-31.png](img%2FScreenshot%20from%202024-03-27%2001-10-31.png)
# Service Configuration Updates:

## Log rotation mechanisms
Log rotation was already enabled in previous lab by this setting in `docker-compose.yml`
```yaml
        max-size: "200k"
```

## Specify memory limits for containers
Memory limits were enabled by this setting in `docker-compose.yml`
```yaml
    deploy:
      resources:
        limits:
          memory: 1G
```

## Health-checks

Health checks are implemented using wget and bash tcp

![Screenshot from 2024-03-27 01-30-05.png](img%2FScreenshot%20from%202024-03-27%2001-30-05.png)