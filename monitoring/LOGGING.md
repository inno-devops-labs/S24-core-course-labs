# Logging Stack Documentation

## Overview

The stack includes the following components:

- **Promtail**: A log collector that ships logs to Loki.
- **Loki**: A log aggregation system that stores and queries logs.
- **Grafana**: A visualization tool that provides dashboards for querying and displaying logs.

## Components

### Promtail

**Role**: Promtail is responsible for collecting logs from various sources and shipping them to Loki. It is configured to scrape logs from Docker containers and send them to Loki for storage and analysis.

**Configuration**:
- **Volumes**:
  - `/var/lib/docker/containers:/var/lib/docker/containers`: Mounts the host's Docker container logs directory to the container's directory.
  - `./promtail-config.yml:/etc/promtail/config.yml`: Mounts the `promtail-config.yml` file from the host to the container's `/etc/promtail/config.yml` file.
- **Command**: `-config.file=/etc/promtail/config.yml`

### Loki

**Role**: Loki is a log aggregation system that stores logs and provides a query interface. It is designed to be cost-effective and easy to operate, making it ideal for storing and querying logs in a distributed system.


### Grafana

**Role**: Grafana is a visualization tool that provides dashboards for querying and displaying logs stored in Loki. It allows users to create custom dashboards and alerts based on log data.
