# Logging

## Components

### Grafana

In this logging stack, Grafana visualizes the logs/metrics in the web interface exposed at port `3000`. It provides the UI for data aggregation and visualization. Displays the queries results from loki.


### Loki

It is responsible for aggregating and storing the logs. Handles the queries.

### Promtail

It processes the local logs and transfers them to loki.


## Screenshots

### Grafana logs

![](images/grafana-logs.png)

### Loki logs

![](images/loki-logs.png)

### Promtail logs

![](images/promtail-logs.png)

### Python app logs

![](images/app_python-logs.png)

### Javascript app logs

![](images/app_javascript-logs.png)
