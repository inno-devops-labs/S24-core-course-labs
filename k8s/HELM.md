# Helm Deployment

## Output of kubectl get pods,svc

```bash
$ kubectl get pods,svc

NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-686d7bc657-fqft4   1/1     Running   0          65s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/app-python   NodePort    10.111.154.200   <none>        80:32664/TCP   65s
service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP        4h31m
```