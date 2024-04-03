# Kubernetes

## Create Deployment and Service resources, check them by get:
```sh
$ kubectl create deployment python-app --image itoqsky/python-app:latest
deployment.apps/python-app created

$ kubectl get deployments
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
python-app   1/1     1            1           6s

$ kubectl expose deployment python-app --type=LoadBalancer --port=5555
service/python-app exposed

$ kubectl get service
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          67s
python-app   LoadBalancer   10.110.40.178   <pending>     5555:32677/TCP   5s
```
## kubectl get pods,svc:
```sh
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/python-app-5c6b7c76c9-slb2x   1/1     Running   0          81s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          98s
service/python-app   LoadBalancer   10.110.40.178   <pending>     5555:32677/TCP   36s
```
### Remove services and deployments:
```sh
$ kubectl delete service --all
service "kubernetes" deleted
service "python-app" deleted

$ kubectl delete deployment --all
deployment.apps "python-app" deleted
```
## Deployment and Service manifest:
```sh
$ kubectl apply -f deployment.yml
deployment.apps/deployment-app-python created

$ kubectl apply -f service.yml
service/service-app-python created
```
## kubectl get pods,svc:
```sh
$ kubectl get pods,svc
NAME                                         READY   STATUS    RESTARTS   AGE
pod/deployment-app-python-7584746c9b-5gcjx   1/1     Running   0          8s
pod/deployment-app-python-7584746c9b-b5nqf   1/1     Running   0          8s
pod/deployment-app-python-7584746c9b-rw5rg   1/1     Running   0          8s

NAME                         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes           ClusterIP      10.96.0.1      <none>        443/TCP          4s
service/service-app-python   LoadBalancer   10.96.56.138   <pending>     5555:32236/TCP   4s
```
## minikube service --all:
```sh
$ minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | service-app-python |        5555 | http://192.168.49.2:32236 |
|-----------|--------------------|-------------|---------------------------|
🎉  Opening service default/service-app-python in default browser...
```
## Browser check:

![check.jpg](assets/check.jpg)