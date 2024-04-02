# Kubernetes

## Basic setup

```bash
kubectl create deployment moscow-time-app --image=damirafliatonov/moscow-time-app:latest
kubectl expose deployment moscow-time-app --type=LoadBalancer --port=8000
```

### Outputs

#### `kubectl get pods,svc`

```bash
NAME                      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes        ClusterIP      10.96.0.1       <none>        443/TCP          5h36m
service/moscow-time-app   LoadBalancer   10.109.134.70   <pending>     8000:31690/TCP   45s
```

### Cleaning

```bash
kubectl delete deployment moscow-time-app
kubectl delete service moscow-time-app
```

## Applying manifest files

```bash
kubectl apply -f app_python/deployment.yml
kubectl apply -f app_python/service.yml
kubectl apply -f app_javascript/deployment.yml
kubectl apply -f app_javascript/service.yml
```

### Outputs

#### `kubectl get pods,svc`

```bash
NAME                                                 READY   STATUS    RESTARTS   AGE
pod/moscow-time-app-deployment-68d6d9b7d8-54ct2      1/1     Running   0          6m12s
pod/moscow-time-app-deployment-68d6d9b7d8-cz4jd      1/1     Running   0          6m12s
pod/moscow-time-app-deployment-68d6d9b7d8-gl6n8      1/1     Running   0          6m12s
pod/moscow-time-app-js-deployment-7c5f8ccc47-6lj4q   1/1     Running   0          54s
pod/moscow-time-app-js-deployment-7c5f8ccc47-mwzlx   1/1     Running   0          54s
pod/moscow-time-app-js-deployment-7c5f8ccc47-xmg4j   1/1     Running   0          54s

NAME                                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes                   ClusterIP   10.96.0.1       <none>        443/TCP          5h46m
service/moscow-time-app-js-service   NodePort    10.98.106.67    <none>        3000:30945/TCP   51s
service/moscow-time-app-service      NodePort    10.97.223.176   <none>        8000:31274/TCP   6m9s
```


#### `minikube service --all`

```bash
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|----------------------------|-------------|---------------------------|
| NAMESPACE |            NAME            | TARGET PORT |            URL            |
|-----------|----------------------------|-------------|---------------------------|
| default   | moscow-time-app-js-service |        3000 | http://192.168.49.2:30945 |
|-----------|----------------------------|-------------|---------------------------|
|-----------|-------------------------|-------------|---------------------------|
| NAMESPACE |          NAME           | TARGET PORT |            URL            |
|-----------|-------------------------|-------------|---------------------------|
| default   | moscow-time-app-service |        8000 | http://192.168.49.2:31274 |
|-----------|-------------------------|-------------|---------------------------|
```


#### `curl http://192.168.49.2:31274`

result:

```html
<!DOCTYPE html>
<html>

<head>
    <style>
        body {
            background-color: #D3D3D3;
            /* Pastel gray */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            color: #000000;
            /* Light blue */
            font-size: 40px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>

<body>
    <h1>2024-04-02 23:53:10</h1>
</body>
```


#### `curl http://192.168.49.2:30945`

```bash
<!DOCTYPE html>
<html>

<head>
    <style>
        body {
            background-color: #D3D3D3;
            /* Pastel gray */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            color: #000000;
            /* Light blue */
            font-size: 40px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>

<body>
    <h1>4/3/2024, 12:13:27 AM</h1>
</body>

</html>
```

## Ingress

```bash
kubectl apply -f ingress.yml
```
- `kubectl get ingress`

```bash
NAME              CLASS    HOSTS                       ADDRESS        PORTS   AGE
example-ingress   <none>   python.app,javascript.app   192.168.49.2   80      8m37s
```

- curl --resolve "python.app:80:$( minikube ip )" -i http://python.app

```
HTTP/1.1 200 OK
Date: Tue, 02 Apr 2024 21:56:41 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 492
Connection: keep-alive

<!DOCTYPE html>
<html>

<head>
    <style>
        body {
            background-color: #D3D3D3;
            /* Pastel gray */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            color: #000000;
            /* Light blue */
            font-size: 40px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>

<body>
    <h1>2024-04-03 00:56:41</h1>
</body>

</html>
```

- `curl --resolve "javascript.app:80:$( minikube ip )" -i http://javascript.app`

```
HTTP/1.1 200 OK
Date: Tue, 02 Apr 2024 21:59:26 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 495
Connection: keep-alive
X-Powered-By: Express
ETag: W/"1ef-X4hOY85V5qJ/EJvAki2PHyJadgI"

<!DOCTYPE html>
<html>

<head>
    <style>
        body {
            background-color: #D3D3D3;
            /* Pastel gray */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            color: #000000;
            /* Light blue */
            font-size: 40px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>

<body>
    <h1>4/3/2024, 12:59:26 AM</h1>
</body>

</html>
```
