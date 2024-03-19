# Monitoring and Logging stack

### Promtail

Promtail collects logs from local sources(docker `json-file`) and sends it to Loki. [./promtail.yml](./promtail.yml) configures logs sources
and processing pipeline.

### Loki

Loki acts as a log storage. It aggregates logs from promtail instance(s), indexes and compress them.

### Grafana

Grafana is a well-known logs visualisation and monitoring tool. Queries data from Loki.

### Java and Python apps

Throw logs into stdin and stderr. Docker stores them using docker `json-file` log driver and Promtail picks up data from
files.

+ Grafana log collection
  ![Screenshot from 2024-03-19 23-06-22.png](img%2FScreenshot%20from%202024-03-19%2023-06-22.png)
+ Loki log collection
  ![Screenshot from 2024-03-19 23-06-30.png](img%2FScreenshot%20from%202024-03-19%2023-06-30.png)
+ Promtail log collection
  ![Screenshot from 2024-03-19 23-06-36.png](img%2FScreenshot%20from%202024-03-19%2023-06-36.png)
+ Java app log collection
  ![Screenshot from 2024-03-19 23-06-42.png](img%2FScreenshot%20from%202024-03-19%2023-06-42.png)
+ Python app log collection
  ![Screenshot from 2024-03-19 23-06-48.png](img%2FScreenshot%20from%202024-03-19%2023-06-48.png)
