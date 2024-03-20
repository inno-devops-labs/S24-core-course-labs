# Log Monitoring System Overview

## Service Descriptions

### Loki

The main role of Loki is to serve as a centralized log storage and query system. It aggregates logs collected by Promtail, making it easier to perform efficient searches and access log data when needed.

### Promtail

Promtail's function is to gather logs from defined sources and transmit them to Loki. It is specifically set up to scrape logs from Docker containers (namely app_python and app_typescript) and the system's log files on the host.

### Grafana

Grafana acts as the visualization tool for the logs stored in Loki. It offers an intuitive interface for users to query, analyze, and explore log data.

## Application Logs: App_Python and App_Typescript

Both of these applications produce logs that are captured by Promtail and subsequently stored within Loki. These logs are accessible for queries and can be visualized through Grafana.

## Visual References

### Docker-compose Configuration for All Containers:

![container.png](assets/container.png)

### Monitor python-app:

![grafana.png](assets/grafana.png)