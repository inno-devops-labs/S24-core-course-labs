# Logging stack report

### content of docker-compose.yml

There are 4 services listed in the docker-compose.yml file:

- **app-python** - python application
  - json-file logging driver
  - log messages are tagged with {{.ImageName}}|{{.Name}}

- **loki**- log aggregation service
  - grafana/loki:2.9.2 image
  - local configuration file (/etc/loki/local-config.yaml)
  - uses the 3100 port

- **promtail** - log collection agent
  - grafana/promtail:2.9.2 image
  - local configuration file (/etc/promtail/config.yml)
  - mounts the local config file (./promtail_config.yml:/etc/promtail/config.yml) and the folder (/var/lib/docker/containers:/var/lib/docker/containers)

- **grafana** - logs visualization service
  - it configures the Loki data source (/etc/grafana/provisioning/datasources/ds.yaml)
  - grafana/grafana:latest image
  - uses the 3000 port

### content of promtail_config.yml

- promtail_config.yml is a Promtail config to collect logs from Docker and forward them to Loki for further analysis.

- Prometheus server listens port 9080 for HTTP requests.

- http://loki:3100/loki/api/v1/push is used in Prometheus to push metrics to Loki

- scrape_configs has the job "docker" and specifies the log file paths inside the docker container

- log lines processing: json parsing, regular expression field extraction, timestamp conversion, label addition.

# screenshots

![app_python](./screenshots/app_python.png)
![loki](./screenshots/loki.png)
![promtail](./screenshots/promtail.png)
![grafana](./screenshots/grafana.png)


