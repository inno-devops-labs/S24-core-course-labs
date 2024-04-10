# Helm

``kubectl get pods,svc``

```
NAME                              READY   STATUS    RESTARTS      AGE
pod/app-nodejs-5f49779887-7cdlk   1/1     Running   1 (16m ago)   6d21h
pod/app-nodejs-5f49779887-xgfkq   1/1     Running   1 (16m ago)   6d21h
pod/app-python-9ffbbdd6-2fsmc     1/1     Running   1 (16m ago)   6d21h
pod/app-python-9ffbbdd6-6phhn     1/1     Running   1 (16m ago)   6d21h
pod/python-app-b7d78c84c-pjbrg    1/1     Running   0             9m16s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-nodejs   LoadBalancer   10.107.133.103   <pending>     3001:32223/TCP   6d21h
service/app-python   LoadBalancer   10.105.125.246   <pending>     3000:32340/TCP   6d21h
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          6d21h
service/python-app   ClusterIP      10.111.99.240    <none>        80/TCP           9m16s
```