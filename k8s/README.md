# Kubernetes

I've managed to complete only part 1 of this lab.

Output of `kubectl get pods,svc`:

```
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-8bb82d16c-zjk11   1/1     Running   0          3m11s

NAME                    TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python      LoadBalancer   10.101.228.201  localhost     8080:31031/TCP   39s
service/kubernetes      ClusterIP      10.96.0.1       <none>        443/TCP          2h41m
```