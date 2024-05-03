# Kubernetes

## Kubernetes Basic Deployment

* Create deployments

```shell
(venv) shredding@SHREDDING-2 k8s % kubectl create deployment app-python --image=shredding228/server_app:latest     
deployment.apps/app-python created
```

* Get deployments

```shell
(venv) shredding@SHREDDING-2 k8s % kubectl get deployments
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
app-python   1/1     1            1           5m11s
```

* Expose pods

```shell
(venv) shredding@SHREDDING-2 k8s % kubectl expose deployment app-python --type=LoadBalancer --port=8080
service/app-python exposed
```

* Get pods, services

```shell
(venv) shredding@SHREDDING-2 k8s % kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-6f49cdf4b8-vch5n   1/1     Running   0          10m

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.99.169.216   <pending>     8080:31152/TCP   2m18s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          11m

```

* Clear deployments, services

```shell
kubectl delete svc python-service go-service
kubectl delete deployment --all
```

## Kubernetes Declarative Deployment

* Apply manifests

```shell
(venv) shredding@SHREDDING-2 k8s % kubectl apply -f app_python/statefulset.yaml
deployment.apps/python-deployment created
(venv) shredding@SHREDDING-2 k8s % kubectl apply -f app_python/service.yaml
service/python-service created

```

* Get pods, services

```shell
(venv) shredding@SHREDDING-2 k8s % kubectl get pods,svc
NAME                                    READY   STATUS    RESTARTS   AGE
pod/python-deployment-cf645b767-4r8jm   1/1     Running   0          38s
pod/python-deployment-cf645b767-7j4hx   1/1     Running   0          38s
pod/python-deployment-cf645b767-ksgct   1/1     Running   0          38s

NAME                     TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python       LoadBalancer   10.99.169.216   <pending>     8080:31152/TCP   17m
service/kubernetes       ClusterIP      10.96.0.1       <none>        443/TCP          25m
service/python-service   LoadBalancer   10.111.209.63   <pending>     8080:31584/TCP   20s

```

* Check service availability

```shell
(venv) shredding@SHREDDING-2 k8s % minikube service --all
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python |        8080 | http://192.168.49.2:31152 |
|-----------|------------|-------------|---------------------------|

```