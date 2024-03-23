# Logging

## Services

### Promtail

* Promtail is responsible for gathering logs from Docker containers and forwarding them to Loki
![promtail](images/promtail.png)

### Loki

* Loki serves as the central log aggregation system. It stores and indexes log data received from Promtail.
![loki](images/loki.png)

### Grafana

* Grafana is used for visualizing logs stored in Loki. It provides a user interface to query and view log data

### Python app

* Logs for app_python 
![app](images/app.png)
