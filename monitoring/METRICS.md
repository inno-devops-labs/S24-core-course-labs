# Metrics Overview

## Prometheus Monitoring Targets

![targets](assets/targets.jpg)

## Dashboard Visualizations

![loki](assets/loki.jpg)

![prometheus](assets/prometheus.jpg)

## Log Management and Memory Allocation

- To control log file size and prevent excessive disk space usage, log rotation settings have been implemented. These settings restrict log file sizes to a maximum of 200KB and maintain a maximum of 10 log files. Older files are deleted as new ones are created. This is configured through the `logging` section in the `docker-compose.yml` file.

- A memory cap of 500MB has been established to limit memory usage. This setting is applied using the `mem_limit` directive in the `docker-compose.yml` file.
