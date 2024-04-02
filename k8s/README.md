# Kubernetes

## Kubernetes Setup and Basic Deployment
```python
minikube start --driver=docker 
kubectl create deployment app-python --image ejedavid/app_python
kubectl expose deployment app-python --type=LoadBalancer --port=8000
```
Running `kubectl get pods,svc`:
```python
dave@dave ~>kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS      AGE
pod/app-python-c6656954d-7spr7   1/1     Running   1 (26s ago)   65s

NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.108.239.4   <pending>     8000:32348/TCP   51s
service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          84s
```

## Declarative Kubernetes Manifests
```python
kubectl apply -f deployment.yml
kubectl apply -f service.yml
```
Running `kubectl get pods,svc` gave:
```python
dave@dave ~>kubectl get pods,svc
NAME                                         READY   STATUS    RESTARTS   AGE
pod/app-python-deployment-677b4b84b5-7bjwd   1/1     Running   0          33s
pod/app-python-deployment-677b4b84b5-ghctf   1/1     Running   0          33s
pod/app-python-deployment-677b4b84b5-pnhc9   1/1     Running   0          33s

NAME                         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python-service   LoadBalancer   10.101.162.250   <pending>     8000:32467/TCP   23s
service/kubernetes           ClusterIP      10.96.0.1        <none>        443/TCP          62s
```

Running `minikube service --all`:
```python
dave@dave ~>minikube service --all
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-python-service |        8000 | http://192.168.49.2:32467 |
|-----------|--------------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🏃  Starting tunnel for service app-python-service.
🏃  Starting tunnel for service kubernetes.
|-----------|--------------------|-------------|------------------------|
| NAMESPACE |        NAME        | TARGET PORT |          URL           |
|-----------|--------------------|-------------|------------------------|
| default   | app-python-service |             | http://127.0.0.1:36095 |
| default   | kubernetes         |             | http://127.0.0.1:43411 |
|-----------|--------------------|-------------|------------------------|
🎉  Opening service default/app-python-service in default browser...
```
Visiting `http://127.0.0.1:36095` from my browser:

[![image.png](https://i.postimg.cc/NF0Yh7PZ/image.png)](https://postimg.cc/zb44KWNk)

## Additional Configuration and Ingress
```python
kubectl apply -f deployment-rust.yml
kubectl apply -f service-rust.yml
```

`minikube service -all` output: 
```python
dave@dave ~>minikube service --all
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-python-service |        8000 | http://192.168.49.2:32467 |
|-----------|--------------------|-------------|---------------------------|
|-----------|------------------|-------------|---------------------------|
| NAMESPACE |       NAME       | TARGET PORT |            URL            |
|-----------|------------------|-------------|---------------------------|
| default   | app-rust-service |        8001 | http://192.168.49.2:31507 |
|-----------|------------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🏃  Starting tunnel for service app-python-service.
🏃  Starting tunnel for service app-rust-service.
🏃  Starting tunnel for service kubernetes.
|-----------|--------------------|-------------|------------------------|
| NAMESPACE |        NAME        | TARGET PORT |          URL           |
|-----------|--------------------|-------------|------------------------|
| default   | app-python-service |             | http://127.0.0.1:38841 |
| default   | app-rust-service   |             | http://127.0.0.1:36277 |
| default   | kubernetes         |             | http://127.0.0.1:34993 |
|-----------|--------------------|-------------|------------------------|
```

```python
kubectl apply -f ingress.yml 
kubectl apply -f ingress-rust.yml 
```
then 
```python
minikube tunnel
``` 
### app_python and app_rust image
[![image.png](https://i.postimg.cc/wM3K4x1p/image.png)](https://postimg.cc/m1x6ts3X)

