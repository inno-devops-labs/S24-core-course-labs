# LOGGING

## Components

### Grafana

Grafana helps visualize and analyze the logs collected by Loki. Has an easier integration with Loki over the network Loki defined in the network 'Loki'.

### Promtail

Collects Logs from the Python Application and send them to Loki, which stores the logs.

### web_app

The web_app service is the Python application which is available at the port 5000 being a part of the Loki network. They generate the logs that are later visible in the Grafana Dashboard.

### Log Settings

Uses the JSON-file driver, customsied for log rotation.

## Screenshots

### Grafana

![](https://i.postimg.cc/FzyWcYdm/Screenshot-from-2024-03-19-22-37-48.png)

### Loki

![](https://i.postimg.cc/VvQZdqND/Screenshot-from-2024-03-19-22-37-57.png)

### Promtail

![](https://i.postimg.cc/ZRyDb7JW/Screenshot-from-2024-03-19-22-38-05.png)

### app_python

![](https://i.postimg.cc/XNdDtz2h/Screenshot-from-2024-03-19-22-37-03.png)
