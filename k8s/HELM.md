# Helm

## Helm chart

```
$ kubectl get pods,svc
NAME                         READY   STATUS    RESTARTS   AGE
pod/app-py-774b8c9bc-4zqvs   1/1     Running   0          20s
pod/app-py-774b8c9bc-6tg64   1/1     Running   0          4m57s
pod/app-py-774b8c9bc-mhm8j   1/1     Running   0          4m57s
pod/app-py-774b8c9bc-zsb2b   1/1     Running   0          4m57s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-py       LoadBalancer   10.106.188.219   <pending>     5000:30928/TCP   4m57s
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          21m
$
```
