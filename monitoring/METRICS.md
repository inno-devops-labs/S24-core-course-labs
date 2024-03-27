# Answers to Lab 8

## 1. Prometheus Targets Page

Prometheus is collecting metrics from every container.

![prometheus_targets.png](imgs/prometheus_targets.png)

## 2. Loki Dashboard

Grafana's Loki dashboard shows Loki's own analytics.

![loki_dashboard.png](imgs/loki_dashboard.png)

## 3. Prometheus Dashboard

Grafana's Prometheus dashboard shows Prometheus's own analytics.

![prometheus_dashboard.png](imgs/prometheus_dashboard.png)

## 4. Log rotation and memory limits.

Memory limit is equal to **800 mb** for each container.
Logs are rotated when the file size reaches **10 MB.**