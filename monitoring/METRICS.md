# Metrics

---

## Logs

There is a specified log rotation

- log size = 1k
- log max number of files = 3

---

## Web App Metrics Scrapping

It is realized by using special library for used
web frameworks

### Python Web App

Used `prometheus_fastapi_instrumentator` library

### Rust Web App

Used `rocket_prometheus` library

All metrics are in `/metrics` endpoint

---

## Screenshots

Metrics from Prometheus and Loki inside Prometheus targets

![metrics](./pics/PrometheusLokiSelfMetricsCollection.png)

Dashboards for Loki and Prometheus (From Prometheus metrics)
![dashboards](./pics/LokiPrometheusDashboards.png)

Web App Logs

![PrometheusBonus.png](./pics/PrometheusBonus.png)

![LogsBonus.png](./pics/LogsBonus.png)

![PrometheusGrafanaWebApps.png](./pics/PrometheusGrafanaWebApps.png)