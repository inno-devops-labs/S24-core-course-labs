# Logging
## Elements
### Grafana
Grafana visualizes logs gathered by Loki, offering an intuitive interface for log analysis. It seamlessly integrates with Loki, eliminating the need for manual configuration.

- Function: Serves as a tool for analyzing and interpreting logs.
- Configuration: Automatically connects to Loki and is accessible through port 3000.

### Loki
Loki is designed for efficient log storage, prioritizing the indexing of log labels to enhance performance.

- Function: Stores logs collected by Promtail.
- Configuration: Operates within Docker, directed by a configuration file that dictates its operational parameters, such as log storage locations and organization. This service is available on port 3100 and uses labels like image_name and container for log categorization.

### Promtail
Promtail is responsible for capturing logs and forwarding them to Loki.

- Function: Gathers and forwards logs.
- Configuration: Configured via a promtail.yml file that specifies log collection sources and preparation methods for Loki. It's tailored to capture logs from Docker containers, specifically targeting app_python and app_rust services, and forwards them to Loki. It is accessible through port 9080.
  
## Services
### app_python and app_rust
These services are designed to be constructed from their respective directories (../app_python and ../app_rust) and are exposed on different ports. They both connect to the loki network.

- Function: Generate logs for monitoring.
- Configuration: Defined within the Docker Compose file, detailing their construction context, port mappings, and logging configurations.

## Logging Configuration
### Logging Method: 
- Employs Docker's JSON-file logging driver, with adjustments for managing log rotation.
### Log Format: 
- Organizes logs in a JSON structure.
### Log Labels: 
- Associates logs with specific labels identifying the image and container names.

## Screenshots
[![app-python-log.jpg](https://i.postimg.cc/XYjJMK9r/app-python-log.jpg)](https://postimg.cc/8jYDM6KG)
[![app-rust-log.jpg](https://i.postimg.cc/mgmrTcS8/app-rust-log.jpg)](https://postimg.cc/dhTFBVpy)
[![loki-log.jpg](https://i.postimg.cc/q7gvqkb0/loki-log.jpg)](https://postimg.cc/xkD2FSVF)
[![promtail-log.jpg](https://i.postimg.cc/yN5YSwtR/promtail-log.jpg)](https://postimg.cc/hJLqk3S4)