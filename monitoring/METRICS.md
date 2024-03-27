## Prometheus Setup
```
http://localhost:9090/targets
```
![sdf](./image3.png)

## Grafana Dashboards

Dashboard for Loki

![sdf](./image4.png)

Dashboard for Prometheus

![sdf](./image5.png)

## Service Configuration Updates

In the docker-compose.yml file, I implemented mechanisms for log rotation and memory limits for all services.

The memory limit for each container is set to 200MB, and log rotation is configured to maintain up to 10 files, each with a maximum size of 15MB.