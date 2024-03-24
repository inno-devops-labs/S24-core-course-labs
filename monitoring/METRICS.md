## Service configuration updates

### Logs
Logs are enhanced by enforcing max size per log file and max amount of file until they are rewritten with the new logs
```yaml
options:
    max-size: 10M
    max-file: 5
```
### Containers
Containers now have the memory consumption limit of 200 MB
```yaml
resources:
  limits:
    memory: 200M
```
## Screenshots

### Prometheus targets
![](screenshots/prometheus_targets.png)

### Loki dashboard
![](screenshots/loki_dashboard.png)

### Prometheus dashboard
![](screenshots/prometheus_dashboard.png)

