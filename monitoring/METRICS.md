# Metrics setup

## Prometheus and Loki

![prometheus_loki.png](screenshots/prometheus_loki.png)

## Grafana dashboards

![grafana_prometheus_dashboard.png](screenshots/grafana_prometheus_dashboard.png)

![grafana_loki_dashboard.png](screenshots/grafana_loki_dashboard.png)

## Service Configuration

### Memory limits

Memory limit of each service is set to 100m via special param.

### Log rotation

Log rotation is setup via max-size and max-file params on logging in docker-compose.

### New prometheus scrapping

Note that scrapping endpoints for custom servers are not setup.

![prometheus_all.png](screenshots/prometheus_all.png)
