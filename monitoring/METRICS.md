# Prometheus metrics

## Screenshots

![Prometheus targets](pics/prometheus_targets.png)

![Grafana promtail dashboard](pics/grafana_promtail_dashboard.png)

![Grafana prometheus dashboard (impoarted)](pics/grafana_prometheus_dashboard_(imported).png)

## Enhancements

Grafana, Loki, and Promtail each have the RAM limit of 100MiB, Prometheus's memory is limited
to 50MiB, limits for app_py and app_go are 30MiB and 20MiB respectively.

## Metrics from web apps

The Python app exports metrics corresponding to the web app (requests count, request handle
time), as well as metrics related to python runtime exposed by the `promteheus_client`, for instance:

![Prometheus, python web_app](pics/prometheus_app_py_sample.png)

The Go app exports metrics corresponding to the web app (requests count, request handle time),
as well as metrics related to go runtime exposed by the prometheus client, for instance:

![Prometheus, go web_app](pics/prometheus_app_go_sample.png)
