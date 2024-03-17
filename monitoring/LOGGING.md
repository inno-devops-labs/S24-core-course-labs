# Logging

## Log Management Infrastructure

### Components

- `Grafana` offers a variety of visualization options for log/metric data, providing users with a graphical interface
  for
  configuring data aggregation and visualization techniques.

- `Loki` is specifically engineered for streamlined log aggregation.

- `Promtail` serves as the intermediary agent transferring local log data to Loki.

### Log Acquisition

Logs collected from all active Docker containers by Promtail. Containers are configured to output logs in the
following JSON format:

```json
{
  "log": "log message from the application",
  "stream": "stdout",
  "attrs": {
    "tag": "image_name|container_name"
  },
  "time": "yyyy-mm-ddThh:mm:ss.nsZ"
}
```

### Log Parsing

The `promtail.yml` file configures `Promtail` to gather Docker logs from localhost, handle them, and forward them to
a `Loki` server. `Promtail` is configured to process Docker logs and organize them based on stream, time, image_name,
container_name, and container_id.

## Screenshots

All screenshots can be found in `screenshots` folder.