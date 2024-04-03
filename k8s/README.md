# Kubernetes

1. Creating a deployment for the app: 'app_python' using ```kubectl create deployment```:
```
$ kubectl create deployment app-python --image sharmatanmay617/app_python:latest
deployment.apps/app-python created
```

To check whether the deployed is running:
```
$ kubectl get deployments
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
app-python   1/1     1            1           8m7s
```

```
$ kubectl get all
NAME                              READY   STATUS    RESTARTS       AGE
pod/app-python-7d88479dfc-j8jcf   1/1     Running   1 (109s ago)   8m9s

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   11m

NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/app-python   1/1     1            1           8m17s

NAME                                    DESIRED   CURRENT   READY   AGE
replicaset.apps/app-python-7d88479dfc   1         1         1       8m11s
```

3. Verifying the service is:

```
$ kubectl expose deployment app-python --type=LoadBalancer --port=8080 --target-port=8080
service/app-python exposed
```

4. Verify that the service is running:
```
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS        AGE
pod/app-python-7d88479dfc-j8jcf   1/1     Running   1 (2m50s ago)   9m10s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.101.191.92   <pending>     8080:31492/TCP   9s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          12m
```

## Deployments using Declarative Kubernetes Manifests
Creating folders for app-python for deployment and service.

1. Apply Manifests:

```
$ kubectl apply -f app-python/deployment.yml
deployment.apps/app-python-deployment created
```

```
$ kubectl apply -f app-python/services.yml
service/app-python-service created
```

2. Verify that the pods and services are running:

```
kubectl get pods,svc
NAME                                         READY   STATUS    RESTARTS       AGE
pod/app-python-7d88479dfc-j8jcf              1/1     Running   1 (4m9s ago)   10m
pod/app-python-deployment-69bf559f44-9nd9b   1/1     Running   0              52s
pod/app-python-deployment-69bf559f44-g685f   1/1     Running   0              52s
pod/app-python-deployment-69bf559f44-ztg6p   1/1     Running   0              52s

NAME                         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python           LoadBalancer   10.101.191.92   <pending>     8080:31492/TCP   88s
service/app-python-service   LoadBalancer   10.103.113.99   <pending>     5000:30366/TCP     12s
service/kubernetes           ClusterIP      10.96.0.1       <none>        443/TCP          13m
```

4. View the services:

```
$ minikube service --all
git:lab08 
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python |        8080 | http://192.168.49.2:30437 |
|-----------|------------|-------------|---------------------------|
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-python-service |          80 | http://192.168.49.2:30884 |
|-----------|--------------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🎉  Opening service default/app-python in default browser...
🎉  Opening service default/app-python-service in default browser...
```

5. Create a tunnel:
```
$ minikube tunnel
Status:  
  machine: minikube
  pid: 69098
  route: 10.96.0.0/12 -> 192.168.49.2
  minikube: Running
  services: [app-python, app-python-service]
    errors: 
    minikube: no errors
    router: no errors
    loadbalancer emulator: no errors
```

6. Verify avaibility using curl:

```
$ curl http://192.168.49.2:30437 && printf '\n'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Current Time in Moscow</title>
</head>
<body>
    <h1>Current Time in Moscow</h1>
    <p>The current time in Moscow is: 2024-04-03 03:17:46</p>
</body>
</html>
```

7. Verify in browser:

![](https://i.postimg.cc/KjW3W558/Screenshot-from-2024-04-03-03-20-04.png)