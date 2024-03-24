# Pics 

Targets of the prometheus:
![targets](pics/prom-targets.png)

Dashboard for loki 
![loki](pics/loki-dash.png)


Dashboard for prometheus 
![prometheus](pics/prom-dash.png)

## Updates to docker-compose 
* to limit the memory resources available for each container I appended the following to the services description (for the java limits were extended to 200M due to its memory consumption): 
  ```
  deploy:
      resources:
        limits:
          memory: 50M
        reservations:
          memory: 20M
  ```
* and for the logs rotation: 
  ```
  logging:
      driver: "json-file"
      options: 
        max-size: "200k"
  ```

## Bonus task 
Here are the targets after I configured collection (and export) from all the containers including java-app and python-app 
![all-targets](pics/all-targets.png)

Java app metrics: 
![java](pics/java-app-metrics.png)

Python app metrics 
![python](pics/python-app-metrics.png)

Healthchecks: 
![health](pics/health.png)