```bash
DevOps on  lab10 [$✘!+?] took 3m 1.3s 
➜  kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-688b456bbd-nzl64   1/1     Running   0          3m19s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/app-python   ClusterIP   10.100.40.215   <none>        80/TCP    12m
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   13m
```