# Logging

This file outlines the logging stack configured in `docker-compose.yml`:

- **app-python**: Logs generated by the Python application are tagged with `{{.ImageName}}|{{.Name}}`, providing identification.
- **loki**: Acts as a centralized aggregator using `grafana/loki:2.9.2`, collecting and storing logs for analysis.
- **promtail**: Operates as a collection agent utilizing `grafana/promtail:2.9.2`, gathering logs from Docker containers and forwarding them to Loki.
- **grafana**: Serves as a visualization tool with `grafana/grafana:latest`, allowing users to explore and analyze log data visually.
- The configuration in Promtail's `promtail.yml` enables the collection of logs from Docker containers and directs them to Loki for storage and further analysis.