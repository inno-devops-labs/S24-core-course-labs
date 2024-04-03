# Task 1 

`kubectl get pods,svc`

```log
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-765d65c554-ck844   1/1     Running   0          5m58s

NAME                          TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python            LoadBalancer   10.102.132.14    <pending>     5000:30748/TCP   92s
service/kubernetes            ClusterIP      10.96.0.1        <none>        443/TCP          13m
```

# Task 2

`kubectl get pods,svc`
```log
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-6b9b5d7476-f5fw2   1/1     Running   0          68s
pod/app-python-6b9b5d7476-hcslf   1/1     Running   0          68s
pod/app-python-6b9b5d7476-tkzm6   1/1     Running   0          68s

NAME                         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
service/app-python-service   ClusterIP   10.96.139.28   <none>        81/TCP    42s
service/kubernetes           ClusterIP   10.96.0.1      <none>        443/TCP   10h
```

`minikube service --all`
```log
minikube service --all
W0403 09:47:47.010432   26092 main.go:291] Unable to resolve the current Docker CLI context "default": context "default": context not found: open C:\Users\Mirel\.docker\contexts\meta\37a8eec1ce19687d132fe29051dca629d164e2c4958ba141d5f4133a33f0688f\meta.json: The system cannot find the path specified.
|-----------|--------------------|-------------|--------------|
| NAMESPACE |        NAME        | TARGET PORT |     URL      |
|-----------|--------------------|-------------|--------------|
| default   | app-python-service |             | No node port |
|-----------|--------------------|-------------|--------------|
* service default/app-python-service has no node port
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
* service default/kubernetes has no node port
* Starting tunnel for service app-python-service.
* Starting tunnel for service kubernetes.
|-----------|--------------------|-------------|------------------------|
| NAMESPACE |        NAME        | TARGET PORT |          URL           |
|-----------|--------------------|-------------|------------------------|
| default   | app-python-service |             | http://127.0.0.1:65464 |
| default   | kubernetes         |             | http://127.0.0.1:65466 |
|-----------|--------------------|-------------|------------------------|
* Opening service default/app-python-service in default browser...
* Opening service default/kubernetes in default browser...
! Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```

![](./images/image.png)