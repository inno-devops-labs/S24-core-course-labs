# Metrics

I followed this [guide](https://grafana.com/docs/grafana-cloud/quickstart/docker-compose-linux/). It helped add and configure prometheus. But nothing worked on WSL and Windows, so installed VirtualBox with Ubuntu and by some miracle same code is working. Idk how to describe this situation, just no comments...

There is one service down. It happened because, at it is stated in the report of Prometheus, there is no `localhost:5000/metrics` which means that my web app does not have such a route, that is why it doesn't respond.

## Log rotation

```yml
x-logging:
  &default-logging
  driver: "json-file"
  options:
    max-size: "5m"
    max-file: "3"
    tag: "{{.ImageName}}|{{.Name}}"
```

## Memory limit

```yml
x-deploy:
  &default-deploy
  resources:
    limits:
      memory: 100M
```

## Targets
![](/monitoring/screenshots/Prometheus1.png)

## Grafana dashboard
![](/monitoring/screenshots/Prometheus2.png)

## Some console screenshot with working Prometheus
![](/monitoring/screenshots/Prometheus3.png)