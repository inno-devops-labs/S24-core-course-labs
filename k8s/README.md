# Kubernetes

## Manual setup

Firstly you should create pod by using:

```
kubectl create deployment app-python --image blinikar/devops-app
```

Then expose port:

```
kubectl expose deployment app-python --type=LoadBalancer --port=5000 --target-port=5000
```

To check: 

```
kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-57f7c5db46-bfgdd   1/1     Running   0          2m54s

NAME                 TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.99.23.12   <pending>     5000:30801/TCP   61s
service/kubernetes   ClusterIP      10.96.0.1     <none>        443/TCP          10m

kubectl logs app-python-57f7c5db46-bfgdd
 * Serving Flask app 'app'
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.244.0.5:5000
Press CTRL+C to quit
```

Clean up: 

```
kubectl delete deployment app-python
kubectl delete service app-python
```

## Declarative set up:

```
kubectl apply -f app-python-deployment.yml
deployment.apps/web-app-deployment created
kubectl apply -f app-python-service.yml
service/web-app-service created
```

Get pods

```
kubectl get pods,svc
NAME                                     READY   STATUS        RESTARTS   AGE
pod/web-app-deployment-c8ddb94bc-6v8jx   1/1     Running       0          3m2s
pod/web-app-deployment-c8ddb94bc-scf5w   1/1     Running       0          3m2s
pod/web-app-deployment-c8ddb94bc-vvsrf   1/1     Running       0          3m2s

NAME                      TYPE           CLUSTER-IP   EXTERNAL-IP   PORT(S)          AGE
service/kubernetes        ClusterIP      10.96.0.1    <none>        443/TCP          21m
service/web-app-service   LoadBalancer   10.110.2.8   <pending>     5000:30788/TCP   2m55s
```

Verifying: 

```
minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|-----------------|-------------|---------------------------|
| NAMESPACE |      NAME       | TARGET PORT |            URL            |
|-----------|-----------------|-------------|---------------------------|
| default   | web-app-service |        5000 | http://192.168.49.2:31540 |
|-----------|-----------------|-------------|---------------------------|
🎉  Opening service default/web-app-service in default browser...
👉  http://192.168.49.2:31540

curl http://192.168.49.2:31540
<!DOCTYPE html>
<html>
    <head>
        <title></title>
    </head>
    <body>
        <h1>Welcome to Moscow!</h1>
        <p>Current time is - 31.03.24 13:41:17</p>
    </body>
    <style>
        html {
            background-color: black;
            color: whitesmoke;
        }
    </style>
</html>
```

![browser](assets/browser.png)

## Ingress

Checking the ingress addon: 

```
kubectl get pods,svc -n ingress-nginx
NAME                                            READY   STATUS      RESTARTS   AGE
pod/ingress-nginx-admission-create-65nmq        0/1     Completed   0          58s
pod/ingress-nginx-admission-patch-p26fb         0/1     Completed   0          58s
pod/ingress-nginx-controller-7c6974c4d8-q5mrb   1/1     Running     0          58s

NAME                                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
service/ingress-nginx-controller             NodePort    10.98.2.168      <none>        80:31526/TCP,443:30533/TCP   58s
service/ingress-nginx-controller-admission   ClusterIP   10.107.177.199   <none>        443/TCP                      58s
```

Applying config:

```
kubectl apply -f ingress.yml
```

Verifying:

```
curl --resolve "web.app:80:$( minikube ip )" -i http://web.app
HTTP/1.1 200 OK
Date: Sun, 31 Mar 2024 10:59:40 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 305
Connection: keep-alive

<!DOCTYPE html>
<html>
    <head>
        <title></title>
    </head>
    <body>
        <h1>Welcome to Moscow!</h1>
        <p>Current time is - 31.03.24 13:59:40</p>
    </body>
    <style>
        html {
            background-color: black;
            color: whitesmoke;
        }
    </style>
</html>
```



