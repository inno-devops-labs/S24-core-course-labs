# Metrics

## Prometheus

Created the ```prometheus.yml``` configuration file to scrape the metrics from Loki and Prometheus containers at 20-second intervals.  

Added the Prometheus as a service in ```docker-compose.yml``` and integrated the Prometheus client in the app_python applications. Retrieving the metrics at ```/metric``` endpoint.

### ```Screenshots of Targets```
![Targets](https://i.postimg.cc/ht06GnSM/Screenshot-from-2024-03-27-02-09-29.png)

## Dashboards

Dashboard (Loki)

![Loki](https://i.postimg.cc/g00pFDCM/Screenshot-from-2024-03-27-02-49-22.png)

Dashboard (Prometheus)

![Prometheus](https://i.postimg.cc/g00pFDCM/Screenshot-from-2024-03-27-02-49-22.png)

## Log Rotation

Implemented log rotation and memory constraints for every service within the docker-compose.yml configuration: Each container now has a memory cap of 200MB, and logs are cycled through to maintain a maximum of 10 files, with each file having a size restriction of 10MB.

```
x-deploy: &default-deploy
  resources:
    limits:
      memory: 200M

x-logging: &common_logging
  driver: 'json-file'
  options:
    tag: '{{.ImageName}}|{{.ContainerName}}'
    max-size: '10M'
    max-file: '10'
```

## App Metrics

app_python

![](https://i.postimg.cc/LX0rpFt5/Screenshot-from-2024-03-27-02-48-10.png)