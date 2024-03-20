# Logging Stack Report

## Overview

The logging stack consists of Loki, Promtail, and Grafana, enabling efficient log collection, storage, and visualization.

## Components

- **Loki**: Scalable log aggregation system for efficient storage and indexing.
- **Promtail**: Agent for streaming logs to Loki from various sources.
- **Grafana**: Analytics and visualization platform for querying and visualizing logs.

## Functionality

- **Loki**: Receives and indexes log streams from Promtail agents.
- **Promtail**: Tails log files, parses log lines, and forwards them to Loki.
- **Grafana**: Provides user-friendly interface for exploring and visualizing logs.


## Usage

To use the logging stack:
1. Ensure Docker is installed on the host machine.
2. Deploy the logging stack using the provided `docker-compose.yml` file.
3. Access Grafana at `http://localhost:3000` to visualize logs and create dashboards.


## Screenshots

### Terminal Logs

![terminal_logs](./assets/terminal_logs.png)

### Docker desktop

![docker_desktop](./assets/docker_desktop.png)

### Python app page

![python_app](./assets/python_app.png)

### Javascript app page

![js_app](./assets/js_app.png)

### Monitor python 

![monitor_python](./assets/monitor_python.png)

### Monitor js 

![monitor_js](./assets/monitor_js.png)

### Monitor loki 

![monitor_loki](./assets/monitor_loki.png)

### Monitor grafana 

![monitor_grafana](./assets/monitor_grafana.png)

### Monitor promtail 

![monitor_promtail](./assets/monitor_promtail.png)