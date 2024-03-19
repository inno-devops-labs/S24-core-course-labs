# Logging

I followed this[tutorial](https://grafana.com/docs/loki/latest/installation/docker/), which you recommended in task. There I found several files (docker-compose and promtail-config which are needed as config files in compose) and slightly modified compose file.

In order to check, run `docker-compose -f docker-compose.yml up` in this directory.

However, I couldn't successfully complete part with Grafana. For some reason, Promtail wouldn't connect on Windows and WSL.

Sometimes it considered the config file to be a directory after mounting. Sometimes it just wouldn't transfer the log. Or, maybe, then the problem was with Loki.

I tried using `sudo` access, putting config to different folders, different compose file options, different promtail configs. Loki making some logs in console but it cant be catched by Grafana.

![](/monitoring/screenshots/1.jpg)
![](/monitoring/screenshots/2.jpg)
![](/monitoring/screenshots/3.jpg)

## Overview of docker-compose.yml

### app-python

- **Purpose:** Represents the Python application.
- **Logging Driver:** Uses the `json-file` logging driver.
- **Options:** Tags log messages with `{{.ImageName}}|{{.Name}}`.

### loki

- **Purpose:** Log aggregator service.
- **Image:** grafana/loki:2.9.2.
- **Ports:** Exposes port 3100.
- **Command:** Uses a local configuration file `/etc/loki/local-config.yaml`.

### promtail

- **Purpose:** Log collection agent.
- **Image:** grafana/promtail:2.9.2.
- **Volumes:** Mounts `./promtail.yml:/etc/promtail/config.yml`(I think promtail can't find this and thus can't locate Loki logs but maybe error somewhere else).
- **Command:** Uses a local configuration file `/etc/promtail/config.yml`.

### grafana

- **Purpose:** Visualization tool for logs.
- **Environment Variables:** 
  - `GF_PATHS_PROVISIONING=/etc/grafana/provisioning`
  - `GF_AUTH_ANONYMOUS_ENABLED=true`
  - `GF_AUTH_ANONYMOUS_ORG_ROLE=Admin`
- **Entrypoint:** Configures datasource for Loki in `/etc/grafana/provisioning/datasources/ds.yaml` (Or error maybe here).
- **Image:** grafana/grafana:latest.
- **Ports:** Exposes port 3000.
