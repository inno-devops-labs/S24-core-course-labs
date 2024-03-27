# Metrics

## Successful setup of Prometheus scrapping logs
  ![prometheus](https://github.com/y4cer/S24-core-course-labs/assets/88382064/1bcc462b-3fc4-4c7e-a1d5-94cbb6ef7fbd)

## Loki dashboard in grafana

  ![loki dashboard](https://github.com/y4cer/S24-core-course-labs/assets/88382064/9bf73c2b-b040-438f-b2a7-6680d4bfd72e)

## Prometheus dashboard in grafana

  ![prometheus dashboard](https://github.com/y4cer/S24-core-course-labs/assets/88382064/e9337cc8-f8d8-4e59-b6af-cfea3654bd3b)


## Log rotation and limits

I changed the logging and deploy configurations in docker-compose.yaml the following way to ensure log rotation and container memory limits: 

```yaml
x-logging:
  &default-logging
  driver: "json-file"
  options:
    max-size: 200k
    max-file: 10
    tag: "{{.ImageName}}|{{.Name}}"

x-deploy:
  &default-deploy
  resources:
    limits:
      memory: 100M
```

## Application metrics

You can see that the promtail service can reach the metrics, below you can see the exported metrics from the applications:

  ![app_python](https://github.com/y4cer/S24-core-course-labs/assets/88382064/e1ef64a6-37a6-4fdd-bd7f-0866415657d1)

  ![app_go](https://github.com/y4cer/S24-core-course-labs/assets/88382064/3d2fb817-a6bb-4b8b-b9e3-4305ad341dcd)

## Healthchecks

You can see all the healthcheck settings in the `docker-compose.yaml` file, to show that they actually work, here is the screenshot:

  ![healtchecks](https://github.com/y4cer/S24-core-course-labs/assets/88382064/9903d869-975b-43fd-9dcc-f7fb124a8f4f)
