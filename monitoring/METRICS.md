# About metrics

## Screenshot of prometheus targets

![target](images/prometheus_targets.png)

## Screenshot of Loki Dashboard

![loki-dashboard](images/loki-dashboard.png)

## Screenshots of Prometheus Dashboard

![prometheus-dashboard-1](images/prometheus-dashboard-1.png)

![prometheus-dashboard-2](images/prometheus-dashboard-2.png)

## Enhancements

### Log rotation (used in each service in logging: options:)

```yml
max-size: "10m"
max-file: "5"
```

### Memory limit (was added by x-deploy)

```yml
x-deploy: &default-deploy
  resources:
    limits:
      memory: 100M

<service-name>:
    deploy: *default-deploy
```

## Apllications metrics (configured by following code) (Bonus)

```python
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), content_type='text/plain')
```

![application_metrics](images/application_metrics.png)
