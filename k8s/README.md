# K8s

## Manual

From guides provided by task:

```
rostislav@rostislavpc:~/devops_labs/k8s/app_python$ minikube start
```

```
rostislav@rostislavpc:~/devops_labs/k8s$ kubectl create deployment manual-flask --image=hallejujah/devops_app:latest
deployment.apps/manual-flask created
rostislav@rostislavpc:~/devops_labs/k8s$ kubectl expose deployment manual-flask --type=LoadBalancer --port=8068
service/manual-flask exposed
rostislav@rostislavpc:~/devops_labs/k8s$ kubectl get services
NAME           TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes     ClusterIP      10.96.0.1       <none>        443/TCP          54s
manual-flask   LoadBalancer   10.99.106.158   <pending>     8068:30110/TCP   18s
rostislav@rostislavpc:~/devops_labs/k8s$ kubectl get pods,svc
NAME                                READY   STATUS    RESTARTS   AGE
pod/manual-flask-75598864fc-nj5sq   1/1     Running   0          44s

NAME                   TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes     ClusterIP      10.96.0.1       <none>        443/TCP          64s
service/manual-flask   LoadBalancer   10.99.106.158   <pending>     8068:30110/TCP   28s
```

Clean up:
```
rostislav@rostislavpc:~/devops_labs/k8s$ kubectl delete service manual-flask
service "manual-flask" deleted
rostislav@rostislavpc:~/devops_labs/k8s$ kubectl delete deployment manual-flask
deployment.apps "manual-flask" deleted
```

## Automatize

Create app_python folder with `deployment.yml` and `service.yml` inside.

```
kubectl apply -f ./app_python
deployment.apps/flask-server-deployment created
service/flask-server-service created
rostislav@rostislavpc:~/devops_labs/k8s$ kubectl get pods,svc
NAME                                           READY   STATUS    RESTARTS   AGE
pod/flask-server-deployment-68959b4dfb-6r845   1/1     Running   0          25s
pod/flask-server-deployment-68959b4dfb-85c8w   1/1     Running   0          25s
pod/flask-server-deployment-68959b4dfb-gmpmc   1/1     Running   0          25s

NAME                           TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/flask-server-service   LoadBalancer   10.109.75.119   <pending>     5000:30444/TCP   25s
service/kubernetes             ClusterIP      10.96.0.1       <none>        443/TCP          4m22s
rostislav@rostislavpc:~/devops_labs/k8s$ minikube service --all
|-----------|----------------------|-------------|---------------------------|
| NAMESPACE |         NAME         | TARGET PORT |            URL            |
|-----------|----------------------|-------------|---------------------------|
| default   | flask-server-service |        5000 | http://192.168.49.2:30444 |
|-----------|----------------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🏃  Starting tunnel for service flask-server-service.
🏃  Starting tunnel for service kubernetes.
|-----------|----------------------|-------------|------------------------|
| NAMESPACE |         NAME         | TARGET PORT |          URL           |
|-----------|----------------------|-------------|------------------------|
| default   | flask-server-service |             | http://127.0.0.1:41925 |
| default   | kubernetes           |             | http://127.0.0.1:36919 |
|-----------|----------------------|-------------|------------------------|
🎉  Opening service default/flask-server-service in default browser...
👉  http://127.0.0.1:41925
🎉  Opening service default/kubernetes in default browser...
👉  http://127.0.0.1:36919
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
```

Here are screenshots:

![](/k8s/screenshots/output.jpg)
![](/k8s/screenshots/screenshot.jpg)