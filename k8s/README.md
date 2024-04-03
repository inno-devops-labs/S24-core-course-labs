# Kubernetes

## `kubectl get pods,svc` output

```
kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/web-mierley-f4675f6b7-x66jx   1/1     Running   0          24m

NAME                  TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes    ClusterIP      10.96.0.1      <none>        443/TCP          26m
service/web-mierley   LoadBalancer   10.110.97.52   <pending>     8080:31956/TCP   16m
```

## `kubectl get pods,svc` output with manifest

```
kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/web-mierley-9fbd45799-9qpd6   1/1     Running   0          2m43s
pod/web-mierley-9fbd45799-dkg7s   1/1     Running   0          2m43s
pod/web-mierley-9fbd45799-n4t6n   1/1     Running   0          2m43s

NAME                          TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
service/kubernetes            ClusterIP   10.96.0.1        <none>        443/TCP   10h
service/web-mierley-service   ClusterIP   10.106.203.200   <none>        81/TCP    2m39s
```

## `minikube service --all` output with manifest files
```
minikube service --all
W0403 09:54:19.942202   17628 main.go:291] Unable to resolve the current Docker CLI context "default": context "default": context not found: open C:\Users\Mirel\.docker\contexts\meta\37a8eec1ce19687d132fe29051dca629d164e2c4958ba141d5f4133a33f0688f\meta.json: The system cannot find the path specified.
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
* service default/kubernetes has no node port
|-----------|---------------------|-------------|--------------|
| NAMESPACE |        NAME         | TARGET PORT |     URL      |
|-----------|---------------------|-------------|--------------|
| default   | web-mierley-service |             | No node port |
|-----------|---------------------|-------------|--------------|
* service default/web-mierley-service has no node port
* Starting tunnel for service kubernetes.
* Starting tunnel for service web-mierley-service.
|-----------|---------------------|-------------|------------------------|
| NAMESPACE |        NAME         | TARGET PORT |          URL           |
|-----------|---------------------|-------------|------------------------|
| default   | kubernetes          |             | http://127.0.0.1:49744 |
| default   | web-mierley-service |             | http://127.0.0.1:49746 |
|-----------|---------------------|-------------|------------------------|
* Opening service default/kubernetes in default browser...
* Opening service default/web-mierley-service in default browser...
! Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```

![](img.png)