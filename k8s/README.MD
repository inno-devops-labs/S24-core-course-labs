# Kubernetes setup

## Task 1

```bash
➜ k8s git:(lab9) kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-5cf559988-b5jkv   1/1     Running   0          35s

NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.97.250.52   <pending>     5000:32619/TCP   16s
service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          7m22s
```

## Task 2

```bash
➜ k8s git:(lab9) kubectl get pods,svc
NAME                                         READY   STATUS    RESTARTS   AGE
pod/app-python-deployment-7dd56975bc-hbfcs   1/1     Running   0          9s
pod/app-python-deployment-7dd56975bc-hhc8z   1/1     Running   0          9s
pod/app-python-deployment-7dd56975bc-qcd9p   1/1     Running   0          9s

NAME                         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python-service   LoadBalancer   10.105.105.228   <pending>     5000:30961/TCP   9s
service/kubernetes           ClusterIP      10.96.0.1        <none>        443/TCP          10m
➜ k8s git:(lab9) minikube service --all
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-python-service |        5000 | http://192.168.49.2:30961 |
|-----------|--------------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🎉  Opening service default/app-python-service in default browser...
Opening in existing browser session.
```

![app_python](img/app_python.png)
