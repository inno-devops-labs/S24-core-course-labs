# Metrics
## Prometheus targets
![Screenshot from 2024-03-23 20-41-13.png](images%2Fassignment8%2FScreenshot%20from%202024-03-23%2020-41-13.png)
## Loki dashboard
![Screenshot from 2024-03-23 21-09-29.png](images%2Fassignment8%2FScreenshot%20from%202024-03-23%2021-09-29.png)
## Prometheus dashboard
![Screenshot from 2024-03-23 21-05-53.png](images%2Fassignment8%2FScreenshot%20from%202024-03-23%2021-05-53.png)
## Enhancements
### `x-logging`
```x-logging:
  &default-logging
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "5"
    tag: "{{.ImageName}}|{{.Name}}"
```
### `x-deploy`
```
x-deploy:
  &default-deploy
  resources:
    limits:
      memory: 200M
```

## Metric gathering for python application
```
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), content_type='text/plain')
```