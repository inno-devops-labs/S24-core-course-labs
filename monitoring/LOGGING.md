## Logging

Logging configuration displays logs from Docker containers. 

## Stack

- **Grafana**: vizualization of logs using dashboards and panels
- **Loki**: storing the logs, that is taking from Promtail
- **Promtail**: collecting logs from Docker containers

## Services

- **app_python**: Flask application from which logs will be taken
- Loki
- Grafana
- Promtail

## Usage

Access to Grafana: localhost:3000. For watching logs choose in Grafana/Explore filter and push "Run query" button

## Screenshots
![alt text](image-1.png)
![alt text](image-2.png)
