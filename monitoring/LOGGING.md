# Monitoring

I have configured monitoring using Grafana, Loki and Promtail. There are 2 web applications that will be monitored.

## Table of Contents

- [Monitoring](#monitoring)
  - [Table of Contents](#table-of-contents)
  - [Components](#components)
  - [Usage](#usage)

## Components

In this system, we have the following components (according to the docker-compose file):

- Grafana: This provides the dashboard for the monitoring system
- Loki: This is the log aggregation system that stores logs from the applications and let us query them
- Promtail: This is the agent that collects logs from the applications and sends them to Loki
- app_python: This is the python web app that returns the current Moscow Time
- app_bun: This is the bonus bun web app that returns the current Moscow Time

Here, Promtail actually collects logs for the docker containers and not directly from the applications. Apart from the web apps, it also collects logs from the Loki and Grafana containers.

## Usage

After running `docker-compose up`, I went to `localhost:3000` on my browser to access the Grafana dashboard. Then I created a new dashboard using `Loki` as a source. Selecting `container_name` as the label, I could select `/monitoring_app_python` and `/monitoring_app_bun` as the source for the logs.

![App Python](https://i.postimg.cc/Kvps47GZ/image.png)

![App Bun](https://i.postimg.cc/dVTn1zNB/image.png)

Because, the system is configured to collect logs from the docker containers, I can see logs from the Loki and Grafana containers as well.

![All containers](https://i.postimg.cc/Nf2R7R8G/image.png)
