## Logging

Current logging configuration displays logs from Docker containers. 

## Stack

- **Grafana**: vizualization of logs using dashboards and panels
- **Loki**: storing the logs, that is taking from Promtail, and offers a query interface
- **Promtail**: collecting logs from Docker containers

## Services

- **app_python**: Flask application from which logs will be taken
- **Loki**
- **Grafana**
- **Promtail**

## Usage

Access to Grafana: localhost:3000. For watching logs choose in Explore filter for logs and push Run query button

## Screenshots


![img.png](./screenshots/logs.png)
![img.png](./screenshots/labels.png)