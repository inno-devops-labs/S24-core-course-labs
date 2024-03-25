### `kubectl get pods,svc`:
```
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-559bb45fc4-6rbfz   1/1     Running   0          21m
NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.99.40.234   <pending>     8000:32106/TCP   18m
service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          115m
```