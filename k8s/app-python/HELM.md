```bash
majorro@new-pekan:~/devops$ kubectl get pods,svc
NAME                                        READY   STATUS    RESTARTS   AGE
pod/app-pyton-app-python-5857f997c8-cm5ch   1/1     Running   0          97s

NAME                           TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/app-pyton-app-python   ClusterIP   10.107.252.143   <none>        8000/TCP   97s
service/kubernetes             ClusterIP   10.96.0.1        <none>        443/TCP    9h
```