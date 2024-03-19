# Logging Report

## Stack

### Promtail

Promtail is the agent responsible for tailing log files and sending log entries to Loki for processing and storage. It plays a crucial role in the collection of log data. Promtail scans log files and extracts relevant labels and timestamps, enhancing the search and query capabilities provided by Loki.

### Loki

Loki is the log aggregation system that stores log entries in a manner optimized for high-speed queries. It provides efficient indexing and search functionality, making it easy to access and analyze log data. Loki serves as the storage backend for log entries and is tightly integrated with Grafana for visualization.

### Grafana

Grafana is a powerful open-source platform for monitoring and observability, which is used for visualizing and exploring log data stored in Loki. It allows users to create dashboards and alerts based on log data, offering a comprehensive solution for log analysis and monitoring.

## Main Task Screenshots

![image](https://github.com/frog-da/DevOps/assets/84839431/901c09c9-d510-4678-ba50-dc6f3a55b711)

- Python app logs:
  ![image](https://github.com/frog-da/DevOps/assets/84839431/8566b7f4-dae7-407a-8aaa-79c09497bcb0)

## Bonus Task Screenshots

![image](https://github.com/frog-da/DevOps/assets/84839431/6c356c2a-c429-4951-a850-024bf644db46)

- Go app logs:
  ![image](https://github.com/frog-da/DevOps/assets/84839431/7d6dc644-8bd4-469e-9ff5-efe0c9afa931)
- Grafana logs:
  ![image](https://github.com/frog-da/DevOps/assets/84839431/8c4eb922-7955-42b4-98d6-222eca6574f1)
- Loki logs:
  ![image](https://github.com/frog-da/DevOps/assets/84839431/0b797387-4882-4634-942e-3a3c2f6d6d0d)
- Promtail logs:
  ![image](https://github.com/frog-da/DevOps/assets/84839431/2163d8f6-05e4-437c-8bc2-21db02d775a4)
