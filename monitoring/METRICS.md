## Metrics lab 8

### Prometheus targets screenshot:
![alt text](image-targets.png)
### Loki dachboard screenshot:
![alt text](image-dashboard-loki.png)
### Prometheus dashboard screenshot:
![alt text](image-dashboard-prometheus.png)

### Log rotation 

Made changes x-logging, the max-size parameter limits the size of log files up to 10 mb, the max-file is a max of 5 log files. Docker automatically creates new files when limits are reached.

```
x-logging: &default-logging
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "5"
    tag: "{{.ImageName}}|{{.Name}}"
```

### Memory limits f

Created x-deploy to docker-compose.yaml for limiting memory usage at 100MB:

```
x-deploy: &default-deploy
  resources:
    limits:
      memory: 100M