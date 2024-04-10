# Helm

## Task 1   
![Screenshot 2024-04-10 at 10.00.11.png](..%2F..%2F..%2F..%2FDesktop%2FScreenshot%202024-04-10%20at%2010.00.11.png)

```bash
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | app-python |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/app-python has no node port
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🏃  Starting tunnel for service app-python.
🏃  Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | app-python |             | http://127.0.0.1:54128 |
| default   | kubernetes |             | http://127.0.0.1:54130 |
|-----------|------------|-------------|-----------------------
```

```bash
kubectl get pods,svc                                                                                                lab10 ◼
 NAME                              READY   STATUS    RESTARTS   AGE
 pod/app-python-568c6dbbfd-89jxn   1/1     Running   0          9m4s
 my-nginx-deploy-785cb5c9f4-rcxg9  1/1     Running   4(10m ago) 6d10h
 NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
 app-python   ClusterIP   10.105.133.162   <none>        80/TCP    28m
 kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP   6d11h
 ```