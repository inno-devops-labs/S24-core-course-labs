# Kubernetes

## Manual setup

```
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/web-app-py-64bf47b878-9gb7c   1/1     Running   0          62s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP        22m
service/web-app-py   LoadBalancer   10.109.167.161   <pending>     80:30520/TCP   39s
```
