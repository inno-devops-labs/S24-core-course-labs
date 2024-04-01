# Task 1

## Create

```bash
APP="app-python"
kubectl create deployment "$APP" --image=bulatok4/app_python:latest --port=8080
kubectl expose deployment "$APP" --type=LoadBalancer --port=8080
kubectl get pods,svc
```

```
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-cluh7h7xp0-ergkr   1/1     Running   0          3m20s

NAME                 TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.99.108.8   <pending>     8080:31664/TCP   1m2s
service/kubernetes   ClusterIP      10.96.0.1     <none>        443/TCP          12m
```

## Delete

```bash
kubectl delete service "$APP"
kubectl delete deployment "$APP"
```
