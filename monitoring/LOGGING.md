# Logging report
## `docker-compose.yml`
### 1. app-java
- **Image**: `djhovi/my-java-app`
- **Ports**: Forwarding traffic from host port 8080 to container port 8080.
- **Role**: This service runs a Java application. It exposes an API or web interface that listens on port 8080.

### 2. app_python
- **Image**: `djhovi/my-flask-app`
- **Volumes**: Mounting a local directory `./logs` into the container's `/app/logs` directory.
- **Ports**: Publishing port 5000 from the container to the host.
- **Role**: This service runs a Flask application. It may expose an API or web interface that listens on port 5000. It also mounts a local directory for logging purposes.

### 3. loki
- **Image**: `grafana/loki:2.9.2`
- **Ports**: Exposing port 3100 for communication.
- **Command**: Specifying a configuration file `-config.file=/etc/loki/local-config.yaml`.
- **Role**: Loki is a log aggregation system. This service aggregates logs from various sources and makes them available for querying and visualization.

### 4. promtail
- **Image**: `grafana/promtail:2.9.2`
- **Volumes**: Mounting local files including `promtail.yml` and Docker container logs.
- **Command**: Specifying a configuration file `-config.file=/etc/promtail/config.yml`.
- **Role**: Promtail is a log shipping agent. It collects logs from various sources, like local files and Docker container logs, and forwards them to Loki for aggregation and storage.

### 5. grafana
- **Image**: `grafana/grafana:latest`
- **Environment Variables**: Configuring Grafana environment variables including data source provisioning and anonymous access.
- **Entrypoint**: Configuring Grafana to use Loki as a data source through a script that generates a configuration file.
- **Ports**: Exposing port 3000 for the Grafana UI.
- **Role**: Grafana is a visualization and monitoring tool. It provides a web-based dashboard to visualize data from various sources, including logs from Loki. This service is configured to use Loki as a data source for log visualization.
## `promtail.yml`
### Server Configuration:
- `http_listen_port`: Specifies the port Promtail should listen on for HTTP connections.
- `grpc_listen_port`: Specifies the port Promtail should listen on for gRPC connections. It's set to `0` here, meaning it's disabled.

### Positions:
- `filename`: Defines the path to the file where Promtail stores the positions of the last log line read for each file. This is used for resuming log reading after restarts.

### Clients:
- `url`: Specifies the URL where Promtail should push logs. In this case, it's configured to push logs to Loki at `http://loki:3100/loki/api/v1/push`.

### Scrape Configurations:
- `job_name`: Specifies the name of the job to be scraped.
- `static_configs`: Defines the list of targets to scrape. In this case, it targets logs from Docker containers.
- `pipeline_stages`: Defines the stages through which logs will be processed.
  - `json`: Parses the incoming logs as JSON, extracting relevant fields like stream, tag, and time.
  - `regex`: Matches and extracts fields from the log file path and tag.
  - `timestamp`: Converts the log timestamp to RFC3339Nano format.
  - `labels`: Assigns labels to the log entry, including stream, time, image_name, container_name, and container_id.
  - `output`: Specifies that the processed log should be sent to the output, which in this case is just the log itself.

## Images:
![Screenshot from 2024-03-19 13-44-57.png](images%2FScreenshot%20from%202024-03-19%2013-44-57.png)
![Screenshot from 2024-03-19 13-45-08.png](images%2FScreenshot%20from%202024-03-19%2013-45-08.png)
![Screenshot from 2024-03-19 13-45-22.png](images%2FScreenshot%20from%202024-03-19%2013-45-22.png)
![Screenshot from 2024-03-19 13-45-32.png](images%2FScreenshot%20from%202024-03-19%2013-45-32.png)
![Screenshot from 2024-03-19 13-45-47.png](images%2FScreenshot%20from%202024-03-19%2013-45-47.png)