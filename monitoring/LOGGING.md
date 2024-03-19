# Documentation and Reporting

## Logging Stack Report

This document offers insights into the logging stack configuration outlined in the `docker-compose.yml` file.

### docker-compose.yml

#### webapp

- **Objective:** Represents the Python application.
- **Logging Mechanism:** Utilizes the `json-file` logging mechanism.
- **Customization:** Marks log messages with `{{.ImageName}}|{{.Name}}`.

#### loki

- **Objective:** Log aggregation service.
- **Image:** grafana/loki:2.9.2.
- **Ports:** Port 3100 is exposed.
- **Setup:** Operates with a local configuration file `/etc/loki/local-config.yaml`.

#### promtail

- **Objective:** Log collection agent.
- **Image:** grafana/promtail:2.9.2.
- **Volumes:** Mounts `./promtail.yml:/etc/promtail/config.yml` and `/var/lib/docker/containers:/var/lib/docker/containers`.
- **Setup:** Utilizes a local configuration file `/etc/promtail/config.yml`.

#### grafana

- **Objective:** Visualization tool for logs.
- **Environment Variables:** 
  - `GF_PATHS_PROVISIONING=/etc/grafana/provisioning`
  - `GF_AUTH_ANONYMOUS_ENABLED=true`
  - `GF_AUTH_ANONYMOUS_ORG_ROLE=Admin`
- **Configuration:** Sets up a datasource for Loki in `/etc/grafana/provisioning/datasources/ds.yaml`.
- **Image:** grafana/grafana:latest.
- **Ports:** Port 3000 is exposed.

### Overview of promtail.yml

This configuration file empowers Promtail to collect and handle logs originating from Docker containers, forwarding them to Loki for storage and analysis purposes.

#### Server Configuration
Defines the ports for Prometheus server listening, with `http_listen_port` configured as `9080` for HTTP requests.

#### Positions Configuration
Specifies the file path pointing to the positions file utilized by the Prometheus server for monitoring the last scrape position of each target.

#### Clients Configuration
Specifies the destination URL to which Prometheus should dispatch metrics. In this case, it is set to http://loki:3100/loki/api/v1/push, designating Loki as the receiver.

## Screenshots

![app_python](./screens/webapp.png)
![grafana](./screens/grafana.png)
![loki](./screens/loki.png)
![promtail](./screens/promtail.png)