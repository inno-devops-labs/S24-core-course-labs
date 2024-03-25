Prometheus scraps metrics successfully
![](assets/prometheus-targets.png)

Loki dashboard:
![img.png](assets/loki-dashboard.png)

Prometheus dashboard:
![img.png](assets/prometheus-dashboard.png)

Log rotation:

For each container I have set up that it has at most 5 log files, each can be 15 MB max and the driver is `local`.
![img.png](assets/log-rotation.png)

Metrics of Python app:
![img.png](assets/python-app-metrics.png)

Healthchecks:
![img.png](assets/healthchecks.png)
