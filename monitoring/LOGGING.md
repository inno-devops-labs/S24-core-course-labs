# Loggging

## Log Management Infrastructure

### Components

- **Promtail** is the agent, which can parse local logs and send them to **Loki**.
  ![promtail](https://github.com/y4cer/S24-core-course-labs/assets/88382064/3daef12c-1302-49aa-8bcc-fe7eff11a14d)

- **Loki** efficient system for log digestion and aggregation.
  ![loki](https://github.com/y4cer/S24-core-course-labs/assets/88382064/2b8cb68e-0586-439c-aa7f-0c7be9142daa)

- **Grafana** visualisation tool for logs and metrics.
  ![grafana](https://github.com/y4cer/S24-core-course-labs/assets/88382064/7dc11745-07af-4951-8d9b-6f1693c6d943)


### Log Acquisition

Logs are collected from all docker containers and stored in the json format which is later parsed by loki

## Screenshots

1. Logs from all containers 
   ![all_containers_logs](https://github.com/y4cer/S24-core-course-labs/assets/88382064/91ef6572-5d6b-48a2-b817-072ba26821b2)

1. `app_python` logs. `app_python` is a simple Python web app which shows current time in moscow
    ![app_python](https://github.com/y4cer/S24-core-course-labs/assets/88382064/9c0e7f04-fa8f-49f5-9383-08b24cccc2d4)

1. `app_go` logs. `app_go` is a simple Go web app which serves static html file.
    ![app_go](https://github.com/y4cer/S24-core-course-labs/assets/88382064/7ebe6abb-bc9a-4ca8-a3bb-fd641e730e5a)
