# Kubernetes

## `kubectl get pods,svc`:

```bash
NAME                             READY   STATUS    RESTARTS   AGE
pod/flask-app-74c769c946-7f9d4   1/1     Running   0          3m26s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/flask-app    NodePort    10.110.151.255   <none>        5000:31621/TCP   8m2s
service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP          10m
```