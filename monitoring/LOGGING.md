# Logging Report

## Components of the Logging Stack

- Loki: Designed for efficient log aggregation, Loki stores log data in a manner optimized for performance and scalability.
- Promtail: Acts as an intermediary agent, transferring local log content to Loki for aggregation and storage.
- Grafana: Serves as the graphical user interface for log and metric visualization. It offers extensive configuration options for data aggregation and visualization techniques.

## Logging Process:

- Docker containers generate logs, which are collected by Promtail.
- The containers utilize standardized logging configurations, resulting in logs being output in JSON format.
- Promtail's configuration file, specifically the scrape_configs section, dictates how log files are located and handled.
- In the provided setup, Promtail is configured to process Docker logs, categorizing them based on attributes like stream, time, image name, container name, and container ID.

## Screenshots

```app_python``` logs

![Alt text](screenshots/app-python-1.png?raw=true)

![Alt text](screenshots/app-python-2.png?raw=true)

```loki``` logs

![Alt text](screenshots/loki-1.png?raw=true)

![Alt text](screenshots/loki-2.png?raw=true)

```grafana``` logs

![Alt text](screenshots/grafana-1.png?raw=true)

![Alt text](screenshots/grafana-2.png?raw=true)

```promtail``` logs

![Alt text](screenshots/promtail-1.png?raw=true)

![Alt text](screenshots/promtail-2.png?raw=true)