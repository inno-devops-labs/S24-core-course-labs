# Lab 8 

## Targets

![](./assets/lab8/task1.png)

## Loki dashboard

![](./assets/lab8/loki_dashboard.png)


## Prometeus dashboard

![](./assets/lab8/prometeus_dashboard.png)

## Logs and memory limits

![](./assets/lab8/logs.png)


## All working targets

![](./assets/lab8/task2.png)

## Add custom metrics

![](./assets/lab8/python_metrics.png)

It is counter for request for this route

## For flutter part

I rewrite THE WHOLE APP to be not a client with flutter ui, to be dart server using shelf

### From this moment all targets are connected
![](./assets/lab8/all_hosts.png)

Let's see flutter metrics
![](./assets/lab8/flutter_metrics.png)

The metrics include:
- greetings_total: This counter keeps track of the total number of greetings. It is incremented each time the /hello endpoint is accessed.
- moscow_total: This counter keeps track of the total number of requests for time in Moscow. It is incremented each time the root / endpoint is accessed.

And now we have...

![](./assets/lab8/metrics_in_prometheus.png)

And this

![](./assets/lab8/logs_metrics.png)