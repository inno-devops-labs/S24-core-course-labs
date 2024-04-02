# Task 1
Result of 
```bash
kubectl get pods,svc
```

```bash
NAME                           READY   STATUS    RESTARTS   AGE
pod/web-app-58dfd5f48c-pdl4z   1/1     Running   0          3m3s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          54m
service/web-app      LoadBalancer   10.103.230.211   <pending>     5001:31983/TCP   2m58s
```

# Task 2
Result of 
```bash
kubectl get pods,svc
```

```bash
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-go-6d8c66f9f9-bzh7h      1/1     Running   0          2m55s
pod/app-go-6d8c66f9f9-thxvn      1/1     Running   0          2m55s
pod/app-go-6d8c66f9f9-z7hjc      1/1     Running   0          2m55s
pod/app-python-78546c949-hmsvd   1/1     Running   0          9s
pod/app-python-78546c949-pcbf9   1/1     Running   0          15s
pod/app-python-78546c949-x4vcz   1/1     Running   0          12s

NAME                         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-go-service       LoadBalancer   10.105.205.177   <pending>     5002:31489/TCP   2m55s
service/app-python-service   LoadBalancer   10.108.46.148    <pending>     5001:31458/TCP   3m
service/kubernetes           ClusterIP      10.96.0.1        <none>        443/TCP          77m
```

Result of 
```bash
minikube service --all
```

```bash
|-----------|----------------|-------------|---------------------------|
| NAMESPACE |      NAME      | TARGET PORT |            URL            |
|-----------|----------------|-------------|---------------------------|
| default   | app-go-service |        5002 | http://192.168.49.2:31489 |
|-----------|----------------|-------------|---------------------------|
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-python-service |        5001 | http://192.168.49.2:31458 |
|-----------|--------------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🏃  Starting tunnel for service app-go-service.
🏃  Starting tunnel for service app-python-service.
🏃  Starting tunnel for service kubernetes.
|-----------|--------------------|-------------|------------------------|
| NAMESPACE |        NAME        | TARGET PORT |          URL           |
|-----------|--------------------|-------------|------------------------|
| default   | app-go-service     |             | http://127.0.0.1:50996 |
| default   | app-python-service |             | http://127.0.0.1:50998 |
| default   | kubernetes         |             | http://127.0.0.1:51000 |
|-----------|--------------------|-------------|------------------------|
🎉  Opening service default/app-go-service in default browser...
🎉  Opening service default/app-python-service in default browser...
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```

### Screenshots
App Python:
![python.png](imgs%2Fpython.png)

App Go:
![go.png](imgs%2Fgo.png)

Bonus:
```bash
NAME                                        READY   STATUS      RESTARTS   AGE
ingress-nginx-admission-create-sbbht        0/1     Completed   0          39m
ingress-nginx-admission-patch-s9h8x         0/1     Completed   1          39m
ingress-nginx-controller-7c6974c4d8-gp7g8   1/1     Running     0          39m
```