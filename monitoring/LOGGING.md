# Logging stack

## Grafana
- Access log data using user-friendly web-interface, cooperate with Loki,
it can connect to different sources, connect data via multithreading and visualize them via building complex monitoring panels.

## Loki 
- Loki is a log aggregation system designed to store and query logs from all your applications and infrastructure. Inspired by Prometheus


## Promtail
- Promtail is an agent which ships the contents of local logs to a private Grafana Loki instance or Grafana Cloud. It is usually deployed to every machine that runs applications which need to be monitored. It primarily: discovers targets, attaches labels to log streams, pushes them to the Loki instance.

This logging stack is composed of several components, they are work together to collect, store, and visualize logs from various services running within a Docker environment. The stack uses `Grafana Loki` as a centralized log aggregation system, with `Promtail` as the agent for shipping logs to `Loki`, and `Grafana` for visualizing the logs. 

The `docker-compose.yml` file defines the configuration for deploying these components with web service.

## Results observation
- deployed containers ae available in query
    ![](img/all_q.png)
- Python application (shows some requests)
    ![](img/python_app.png)
- Rust Application 
    ![](img/rust_app.png)
- Grafana
    ![](img/grafana.png)
- Loki
    ![](img/loki.png)
- Promtail
    ![](img/promtail.png)
- All docker containers

    Select all deployed containers by selecting job as a filter, 'job' value should be equal to 'containers'
    ![](img/all_containers.png)