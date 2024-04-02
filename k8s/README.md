# Kubernetes

## Kubernetes Setup
Deploying python app:
```shell
minikube start
kubectl create deployment app-python --image AlebrahimLaith/app_python
kubectl expose deployment app-python --type=LoadBalancer --port=5000
```
Then
```shell
D:\S24-core-course-labs\k8s> kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-54f6f75c58-4r72v   1/1     Running   0          33s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.110.132.201   <pending>     5000:31910/TCP   58s
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          40s
```
## Cleanup
```shell
D:\S24-core-course-labs\k8s> kubectl delete deployment app-python
deployment.apps "app-python" deleted
D:\S24-core-course-labs\k8s>kubectl delete service app-python                                                                   
service "app-python" deleted
```

## Declarative Kubernetes Manifests
Then creating folders for app_python deployment and service:
```shell
kubectl apply -f app_python
deployment.apps/app-python-deployment created
service/app-python-service created
```
Then running `kubectl get pods,svc`:
```shell
D:\S24-core-course-labs\k8s> kubectl get pods,svc
NAME                                         READY   STATUS    RESTARTS   AGE
pod/app-python-deployment-8446c9646f-ghcln   1/1     Running   0          1m30s
pod/app-python-deployment-8446c9646f-x4cdw   1/1     Running   0          1m30s
pod/app-python-deployment-8446c9646f-zn9kz   1/1     Running   0          1m30s

NAME                         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python-service   LoadBalancer   10.110.119.36   <pending>     5000:32308/TCP   1m
service/kubernetes           ClusterIP      10.96.0.1       <none>        443/TCP          2m50s
```

Then Running `minikube service --all`:
```shell
D:\S24-core-course-labs\k8s> minikube service --all
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-python-service |        5000 | http://192.168.49.2:32308 |
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
| default   | app-python-service |             | http://127.0.0.1:58767 |
| default   | kubernetes         |             | http://127.0.0.1:33827 |
|-----------|--------------------|-------------|------------------------|
```
![alt text](screenshots/app_python.png)

## Additional Configuration and Ingress
For  bonus task:
```shell
D:\S24-core-course-labs\k8s> kubectl apply -f app_js
deployment.apps/app-js-deployment created
service/app-js-service created
```

Applying ingress manifest: 
```shell
D:\S24-core-course-labs\k8s> kubectl apply -f ingress.yml 
ingress.networking.k8s.io/app-ingress configured
```
then running `minikube tunnel`:

```shell
D:\S24-core-course-labs\k8s> minikube service --all 
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-python-service |        5000 | http://192.168.49.2:32308 |
|-----------|--------------------|-------------|---------------------------|

|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-js-service     |        5001 | http://192.168.49.2:31062 |
|-----------|--------------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
<...>
|-----------|--------------------|-------------|------------------------|
| NAMESPACE |        NAME        | TARGET PORT |          URL           |
|-----------|--------------------|-------------|------------------------|
| default   | app-python-service |             | http://127.0.0.1:58767 |
| default   | kubernetes         |             | http://127.0.0.1:33827 |
| default   | app-js-service     |             | http://127.0.0.1:58982 |
|-----------|--------------------|-------------|------------------------|
<...>
``` 
