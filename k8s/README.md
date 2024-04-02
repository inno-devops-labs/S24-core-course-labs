# Kubernetes

## Create a Deployment resource and check it:

```
$ kubectl create deployment python-app --image batdockerivankornienko/app_python:latest
deployment.apps/python-app created
```

```
$ kubectl get deployments
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
app-python   1/1     1            1           8m7s
```

## Create a Service resource and check it:

```
$ kubectl expose deployment python-app --type=LoadBalancer --port=80
service/python-app exposed
```

```
$ kubectl get service
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP        9m25s
python-app   LoadBalancer   10.107.159.39   <pending>     80:32495/TCP   82s
```

## The output of the `kubectl get pods,svc`:

```
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/python-app-7c65d8854f-mp995   1/1     Running   0          21m

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP        10m
service/python-app   LoadBalancer   10.107.159.39   <pending>     80:32495/TCP   2m32s
```

### Cleanup:

```
$ kubectl delete service kubernetes
service "kubernetes" deleted
```

```
$ kubectl delete service python-app
service "python-app" deleted
```

```
$ kubectl delete deploy python-app
deployment.apps "python-app" deleted
```

## Create a `deployment.yml` manifest:

```
$ kubectl apply -f deployment.yml
deployment.apps/python-app-deployment created
```

## Create a `service.yml` manifest:

```
$ kubectl apply -f service.yml
service/python-app-service created
```

## The output of the `kubectl get pods,svc`:

```
$ kubectl get pods,svc
NAME                                         READY   STATUS    RESTARTS   AGE
pod/python-app-deployment-6ccfc4b655-6s58x   1/1     Running   0          4m13s
pod/python-app-deployment-6ccfc4b655-m57f9   1/1     Running   0          4m9s
pod/python-app-deployment-6ccfc4b655-rpmt2   1/1     Running   0          4m6s

NAME                         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes           ClusterIP      10.96.0.1       <none>        443/TCP          28m
service/python-app-service   LoadBalancer   10.107.249.39   <pending>     8000:30128/TCP   28m
```

## The output of the `minikube service --all`:

```
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
| default   | python-app-service |        8000 | http://192.168.49.2:30128 |
|-----------|--------------------|-------------|---------------------------|
🎉  Opening service default/python-app-service in default browser...
```

## Verify from browser:

![image.png](screenshots/image.png)
