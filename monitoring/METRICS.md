# Metrics

## Prometheus Status

![prometheus status](./screenshots//prometheus.png)


## Grafana Dashboard
![grafana dashboard](./screenshots/dashboard_grafana.png)


## Loki dashboard
![loki dashboard](./screenshots/dashboard_loki.png)


## Prometheus dashboard
![prometheus dashboard](./screenshots/dashboard_prometheus.png)

### Healthcheck
The following healthcheck is implemented in the `docker-compose.yml` file:
```yml
healthcheck:
      test: ["CMD", "curl", "-f", "<container_name>:<port>"]
      interval: 30s
      timeout: 15s
      retries: 3
```