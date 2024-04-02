## Prometheus scrapping  all metrics

![prometheus](screenshots/targets.png)

## Grafana Dashboards for loki and prometheus

![loki_dashboard](screenshots/lokidashboard.png)

![promotheus_dashboard](screenshots/prometheusdashboard.png)

## Log rotation
```yaml
        logging:
            driver: "json-file"
            options:
                max-size: "200k"
                max-file: "10"
```

## Memory limit
```yaml
        mem_limit: 500m
```
