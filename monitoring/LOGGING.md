# Logging Report

## Stack

### Promtail

Promtail is the agent responsible for tailing log files and sending log entries to Loki for processing and storage. It plays a crucial role in the collection of log data. Promtail scans log files and extracts relevant labels and timestamps, enhancing the search and query capabilities provided by Loki.

### Loki

Loki is the log aggregation system that stores log entries in a manner optimized for high-speed queries. It provides efficient indexing and search functionality, making it easy to access and analyze log data. Loki serves as the storage backend for log entries and is tightly integrated with Grafana for visualization.

### Grafana

Grafana is a powerful open-source platform for monitoring and observability, which is used for visualizing and exploring log data stored in Loki. It allows users to create dashboards and alerts based on log data, offering a comprehensive solution for log analysis and monitoring.

## Main Task Screenshots
