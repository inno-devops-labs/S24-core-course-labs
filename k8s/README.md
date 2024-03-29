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

## Manifest-based setup

```
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/web-app-py-54bf57f5d4-g8ktf   1/1     Running   0          3m23s
pod/web-app-py-54bf57f5d4-k8ngh   1/1     Running   0          3m23s
pod/web-app-py-54bf57f5d4-p4d6p   1/1     Running   0          3m23s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          4m43s
service/web-app-py   LoadBalancer   10.105.228.85   <pending>     5000:31951/TCP   3m23s
$ minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | web-app-py |        5000 | http://192.168.49.2:31951 |
|-----------|------------|-------------|---------------------------|
🎉  Opening service default/web-app-py in default browser...
Opening in existing browser session.
$
```
