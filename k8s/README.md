# Task 1

Create python app deployment:
```
user@user-PC:~/S24-core-course-labs/k8s$ kubectl create deployment app-python --image=masterlogick/devops-py-img
deployment.apps/app-python created
```
```
user@user-PC:~/S24-core-course-labs/k8s$ kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-8c86848d5-wfhpp   1/1     Running   0          13s

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   6m
```

Create load balancer:
```
user@user-PC:~/S24-core-course-labs/k8s$ kubectl expose deployment app-python --type=LoadBalancer --port=8080
service/app-python exposed
user@user-PC:~/S24-core-course-labs/k8s$ kubectl get services
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
app-python   LoadBalancer   10.107.91.139   <pending>     8080:32368/TCP   8s
kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          8m4s
```
```
user@user-PC:~/S24-core-course-labs/k8s$ minikube service app-python
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python |        8080 | http://192.168.49.2:32368 |
|-----------|------------|-------------|---------------------------|
🎉  Opening service default/app-python in default browser...
```
Check that deployment and service are running
```
user@user-PC:~/S24-core-course-labs/k8s$ kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-8c86848d5-wfhpp   1/1     Running   0          3m41s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.107.91.139   <pending>     8080:32368/TCP   92s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          9m28s
```

Cleanup:
```
user@user-PC:~/S24-core-course-labs/k8s$ kubectl delete service app-python
service "app-python" deleted
```
```
user@user-PC:~/S24-core-course-labs/k8s$ kubectl delete deployment app-python
deployment.apps "app-python" deleted
```
```
user@user-PC:~/S24-core-course-labs/k8s$ kubectl get pods,svc
NAME                             READY   STATUS        RESTARTS   AGE
pod/app-python-8c86848d5-wfhpp   1/1     Terminating   0          6m11s

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   11m

user@user-PC:~/S24-core-course-labs/k8s$ kubectl get pods,svc
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   12m
```

# Task 2

Create deployment:
```
user@user-PC:~/S24-core-course-labs/k8s$ kubectl apply -f ./app_python/deployment.yml 
deployment.apps/app-python-deployment created
```
Create service:
```
user@user-PC:~/S24-core-course-labs/k8s$ kubectl apply -f ./app_python/service.yml 
service/app-python-service created
```
Check that deployment and service are running
```
user@user-PC:~/S24-core-course-labs/k8s$ kubectl get pods,svc
NAME                                         READY   STATUS    RESTARTS   AGE
pod/app-python-deployment-765c59b469-bjc5h   1/1     Running   0          7m21s
pod/app-python-deployment-765c59b469-bv6x2   1/1     Running   0          7m27s
pod/app-python-deployment-765c59b469-vfccv   1/1     Running   0          7m24s

NAME                         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python-service   LoadBalancer   10.101.72.127   <pending>     8080:31168/TCP   7m2s
service/kubernetes           ClusterIP      10.96.0.1       <none>        443/TCP          34m
```
Open service in browser:
![img.png](img%2Fimg.png)
```
user@user-PC:~/S24-core-course-labs/k8s$ minikube service --all
|-----------|--------------------|---------------------------|---------------------------|
| NAMESPACE |        NAME        |        TARGET PORT        |            URL            |
|-----------|--------------------|---------------------------|---------------------------|
| default   | app-python-service | name-of-service-port/8080 | http://192.168.49.2:31168 |
|-----------|--------------------|---------------------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🎉  Opening service default/app-python-service in default browser...
```

# Bonus tasks

## Create configs for java app

Create deployment:
```
user@user-PC:~/S24-core-course-labs/k8s$ kubectl apply -f ./app_java/deployment.yml 
deployment.apps/app-java-deployment created
```
Create service:
```
user@user-PC:~/S24-core-course-labs/k8s$ kubectl apply -f ./app_java/service.yml 
service/app-java-service created
```
Check that deployment and service are running
```
user@user-PC:~/S24-core-course-labs/k8s$ kubectl get pods,svc
NAME                                         READY   STATUS    RESTARTS   AGE
pod/app-java-deployment-5b44695844-7jv5s     1/1     Running   0          36s
pod/app-java-deployment-5b44695844-kwzz7     1/1     Running   0          36s
pod/app-java-deployment-5b44695844-zj6vq     1/1     Running   0          36s
pod/app-python-deployment-765c59b469-bjc5h   1/1     Running   0          11m
pod/app-python-deployment-765c59b469-bv6x2   1/1     Running   0          11m
pod/app-python-deployment-765c59b469-vfccv   1/1     Running   0          11m

NAME                         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-java-service     LoadBalancer   10.97.62.237    <pending>     8080:30748/TCP   31s
service/app-python-service   LoadBalancer   10.101.72.127   <pending>     8080:31168/TCP   11m
service/kubernetes           ClusterIP      10.96.0.1       <none>        443/TCP          38m
```
Open service in browser:
![img_2.png](img%2Fimg_2.png)
```
user@user-PC:~/S24-core-course-labs/k8s$ minikube service app-java-service
|-----------|------------------|---------------------------|---------------------------|
| NAMESPACE |       NAME       |        TARGET PORT        |            URL            |
|-----------|------------------|---------------------------|---------------------------|
| default   | app-java-service | name-of-service-port/8080 | http://192.168.49.2:30748 |
|-----------|------------------|---------------------------|---------------------------|
🎉  Opening service default/app-java-service in default browser...
```

