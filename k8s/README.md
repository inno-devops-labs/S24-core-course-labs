# Kubernetes setup and basic Deployment

## First setup

``kubectl get pods,svc``

```
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-789d9d996b-2jw4l   1/1     Running   0          51s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.106.65.186   <pending>     3000:31829/TCP   43s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          6m48s
```

## Declarative Kubernetes Manifests

``kubectl get pods,svc``

```
NAME                            READY   STATUS    RESTARTS   AGE
pod/app-python-9ffbbdd6-5cnpv   1/1     Running   0          5s
pod/app-python-9ffbbdd6-9j6pk   1/1     Running   0          5s

NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.96.49.146   <pending>     3000:31038/TCP   5s
service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          15m```
```

``minicube service --all``

```
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python |        3000 | http://192.168.49.2:31038 |
|-----------|------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🏃  Starting tunnel for service app-python.
🏃  Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | app-python |             | http://127.0.0.1:49585 |
| default   | kubernetes |             | http://127.0.0.1:49587 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/app-python in default browser...
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```

![](img/app_python.png)

## Ingress

``kubectl get pods,svc``

```
pod/app-nodejs-5f49779887-7cdlk   1/1     Running   0          8s
pod/app-nodejs-5f49779887-xgfkq   1/1     Running   0          8s
pod/app-python-9ffbbdd6-2fsmc     1/1     Running   0          14s
pod/app-python-9ffbbdd6-6phhn     1/1     Running   0          14s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-nodejs   LoadBalancer   10.107.133.103   <pending>     3001:32223/TCP   8s
service/app-python   LoadBalancer   10.105.125.246   <pending>     3000:32340/TCP   14s
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          24m
```

``minicube service --all``

```
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-nodejs |        3001 | http://192.168.49.2:32223 |
|-----------|------------|-------------|---------------------------|
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python |        3000 | http://192.168.49.2:32340 |
|-----------|------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🏃  Starting tunnel for service app-nodejs.
🏃  Starting tunnel for service app-python.
🏃  Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | app-nodejs |             | http://127.0.0.1:50397 |
| default   | app-python |             | http://127.0.0.1:50399 |
| default   | kubernetes |             | http://127.0.0.1:50401 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/app-nodejs in default browser...
🎉  Opening service default/app-python in default browser...
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```

### Availability check

```
PS C:\Users\evsey> curl.exe -H "Host: python.app" http://192.168.49.2   
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moscow Time</title>
</head>
<body>
    <h1>Current Time in Moscow:</h1>
    <p>2024-04-03 08:59:22</p>
</body>
</html>
PS C:\Users\evsey> curl.exe -H "Host: nodejs.app" http://192.168.49.2 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>World Clock</title>
</head>
<body>
    <h1>Current Time in Different Cities:</h1>
    <ul>

            <li><strong>Moscow:</strong> 4/3/2024, 8:59:32 AM</li>

            <li><strong>Paris:</strong> 4/3/2024, 7:59:32 AM</li>

            <li><strong>London:</strong> 4/3/2024, 6:59:32 AM</li>

            <li><strong>New York City:</strong> 4/3/2024, 1:59:32 AM</li>

    </ul>
</body>
</html>
```