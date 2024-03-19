# Documentation for Logging Stack

## Promtail

Promtail gathers and transmits logs to Loki.

- Accessible through port 9080.
- Monitors log files on the host and forwards log lines to Loki.
- Utilizes a local configuration file [promtail.yml](./promptail.yml) to define
  scrape targets and settings.

## Grafana

Grafana is utilized for visualization and monitoring purposes.

- Accessible through port 3000.
- Provides a web-based interface for querying and visualizing log data.
- Configured with anonymous authentication and admin privileges.
- Establishes a data source for Loki, enabling Grafana to query Loki's stored
  logs.

## Application

The Python app exposes endpoints for application functionality.

- Logs are collected by Docker's default JSON-file logging driver with
  customized rotation settings.
- All logs are written into stdin.
- Both services are part of the loki network, facilitating communication with
  Loki and Grafana.

## Loki

Loki serves as a scalable log aggregation system inspired by Prometheus.

- Receives log streams from Promtail.
- Stores logs in a compressed, indexed format.
- Accessible through port 3100.
- Configuration is managed using a local file.
- The configuration includes two labels: image_name and container_name.

# Integration

Promtail transmits log streams to Loki for storage.

Grafana retrieves log data stored in Loki for visualization and monitoring
purposes.

## Conclusion

Grafana, Loki, and Promtail make up the logging stack, which provides a complete
solution for log gathering, storage, visualisation, and monitoring. This
improves the effectiveness of troubleshooting and log handling for deployed
apps.
