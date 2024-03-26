## Screenshots
![Grafana Dashboard](prometeus1.png)
![Grafana Dashboard](loki.png)
![Grafana Dashboard](targets.png)
![Grafana Dashboard](targets2.png)
![Grafana Dashboard](dashboard1.png)
![Grafana Dashboard](dashboard2.png)

## Snippets
```
    logging:
      driver: "json-file"
      options:
        max-size: "5m"
        max-file: "3"
        tag: "{{.ImageName}}|{{.Name}}"
```

```
deploy:
      resources:
        limits:
          memory: 1000M
```