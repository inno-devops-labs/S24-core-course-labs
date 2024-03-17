# Logging

## Description
The documentation about logging system using Loki, Promtail and Grafana in the `docker-compose.yml`.

## Components
Logging stack contains four components:
* Loki;
* Promtail;
* Grafana;
* Application (app_python).

## Loki
Loki is a log aggregation tool, accessible on 3100 port and built on `grafana/loki:2.9.2` image.
![loki](screenshots/loki.png)

## Promtail
Logs collection tools. Collects logs and sends to `Loki`, built on `grafana/promtail:2.9.2` image, uses local config `promtail.yml` and mounted with volumes:
- ./promtail.yml:/etc/promtail/config.yml
- /var/lib/docker/containers:/var/lib/docker/containers.
![promtail](screenshots/promtail.png)

## Grafana
Graphical visualization and monitoring of logs tool, accessible on 3000 port and built on `grafana/grafana:latest` image.
![grafana](screenshots/grafana.png)

## Application (app_python)
The python application, uses `sokolofff/app_python` image and becomes as a part of `Loki` system.
![app_python](screenshots/app_python.png)

## Configuration
The logging driver is a JSON-file logging driver, where each log is tagged with image and container names.

## System
Promtail collects and sends logs to Loki, while Grafana queries data from Loki for it work (monitoring, visualization, etc).

