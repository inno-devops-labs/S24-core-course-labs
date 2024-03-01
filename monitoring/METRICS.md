# Metrics

## Screenshots

### `Prometheus` and `Loki` metrics in `Grafana`

![img.png](imgs/prometheus_loki_metrics.png)

### `Prometheus` dashboard

![img.png](imgs/prometheus_dashboard.png)

### `Loki` dashboard

![img.png](imgs/loki_dashboard.png)

## Log Rotation and memory limit

All services are configured to have `json-file` logging driver with `100m` maximum size and `10` files.

Also services are limited in memory:

- `app_python`, `app_kotlin` - `300m`
- `grafana`, `prometheus`, `loki`, `promtail` - `500m`
