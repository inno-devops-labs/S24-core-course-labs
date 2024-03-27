# Prometheus

![alt text](screenshots/prometheus.png)

# Grafana

![alt text](screenshots/grafana_prometheus.png)
![alt text](screenshots/grafana_loki.png)

Changes:

- For the 'promtail`service, a log rotation mechanism was added using the`json-file` driver with max-size: "10m" and max-file: "3"
- For the 'promtail` service a memory limit of 512 megabytes is set
- For the 'grafana` service a memory limit of 1 gigabyte is set
- For the 'promtail` service a memory limit of 2 gigabytes is set

![alt text](screenshots/grafana_prometheus2.png)
![alt text](screenshots/grafana_loki2.png)

## Extend Prometheus

![alt text](screenshots/prometheus2.png)
