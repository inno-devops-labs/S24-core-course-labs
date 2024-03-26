# Answers to Lab 8

## 1. Prometheus Targets Page

Metrics from all containers are being scraped by Prometheus.

![prometheus_targets.png](imgs/prometheus_targets.png)

## 2. Loki Dashboard

The Loki dashboard in Grafana displays metrics of Loki itself.

![loki_dashboard.png](imgs/loki_dashboard.png)

## 3. Prometheus Dashboard

The Prometheus dashboard in Grafana displays metrics of Prometheus itself.

![prometheus_dashboard.png](imgs/prometheus_dashboard.png)

## 4. Log rotation and memory limits.

Memory limit is equal to **800 mb** for each container.
Logs are rotated when the file size reaches **10 MB.**
