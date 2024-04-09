# Task 1

```bash
helm install helm-app-python ./helm_app_python/ --values ./helm_app_python/values.yaml
```

## Output

```bash
kubectl get pods,svc
```

```
NAME                                      READY   STATUS    RESTARTS   AGE
pod/my-helm-app-python-6bd3e32042-14h37   1/1     Running   0          54s

NAME                         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/helm-app-python      LoadBalancer   10.99.61.11     <pending>     8080:30201/TCP   14s
service/kubernetes           ClusterIP      10.96.0.1       <none>        443/TCP          8m
```
