## Logging and monitoring

The logging stack consists of tools that used to capture, aggregate and visualize logs.

### Promtail 
Scrapping logs from docker containers and forwarding them to Loki. The configuration is in `promtail-local-config.yaml`.

**Logs**
![promtail_logs.jpeg](images/promtail_logs.jpeg)

### Loki
Aggregate the logs.

![read_logs.jpeg](images/read_logs.jpeg)

### Grafana
Visualize the logs.
![grafana_logs.jpeg](images/grafana_logs.jpeg)