## Part 1
```bash
(venv) smasiner@smasIners-MacBook-Pro k8s % kubectl create deployment app-python --image=smasiner2/python_app:latest --port=8080 
deployment.apps/app-python created
(venv) smasiner@smasIners-MacBook-Pro k8s % ls
(venv) smasiner@smasIners-MacBook-Pro k8s % kubectl expose deployment app-python --type=LoadBalancer --port=8080
service/app-python exposed
(venv) smasiner@smasIners-MacBook-Pro k8s % kubectl get svc
NAME         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
app-python   LoadBalancer   10.106.123.118   <pending>     8080:30642/TCP   22s
kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          7m18s
(venv) smasiner@smasIners-MacBook-Pro k8s % touch README.md
(venv) smasiner@smasIners-MacBook-Pro k8s % kubectl get pods,svc
NAME                              READY   STATUS             RESTARTS   AGE
pod/app-python-76474f8d67-czlgk   0/1     ImagePullBackOff   0          85s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.106.123.118   <pending>     8080:30642/TCP   65s
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          8m1s
(venv) smasiner@smasIners-MacBook-Pro k8s % kubectl delete service app-python
service "app-python" deleted
(venv) smasiner@smasIners-MacBook-Pro k8s % kubectl delete deployment app-python
deployment.apps "app-python" deleted
(venv) smasiner@smasIners-MacBook-Pro k8s % kubectl get pods,svc                
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   10m
(venv) smasiner@smasIners-MacBook-Pro k8s % get deployments
zsh: command not found: get
(venv) smasiner@smasIners-MacBook-Pro k8s % kubectl get deployments
No resources found in default namespace.
```
## Part 2

```bash
(venv) smasiner@smasIners-MacBook-Pro k8s % kubectl get pods,svc  
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-b9f8d9d88-47wxj   1/1     Running   0          17m
pod/app-python-b9f8d9d88-5q2d2   1/1     Running   0          17m
pod/app-python-b9f8d9d88-zkgwp   1/1     Running   0          17m

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.110.168.232   <pending>     8080:32460/TCP   17m
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          35m
(venv) smasiner@smasIners-MacBook-Pro k8s % minikube service --all
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python |        8080 | http://192.168.49.2:32460 |
|-----------|------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🏃  Starting tunnel for service app-python.
🏃  Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | app-python |             | http://127.0.0.1:63735 |
| default   | kubernetes |             | http://127.0.0.1:63737 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/app-python in default browser...
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```
![img.png](img.png)