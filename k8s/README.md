# Lab 9 K8s
## 1st task
`kubectl get pods,svc`
```
NAME                              READY   STATUS    RESTARTS   AGE
pod/hello-node-5cd85f464c-gjtq6   1/1     Running   0          9m22s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/hello-node   LoadBalancer   10.110.64.102   <pending>     8080:31514/TCP   5m33s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          173m
```
## 2nd task
`kubectl get pods,svc`
```NAME                               READY   STATUS    RESTARTS   AGE
pod/java-spring-56fc6c654b-b696t   1/1     Running   0          100m
pod/java-spring-56fc6c654b-fsrx5   1/1     Running   0          100m
pod/java-spring-56fc6c654b-gfmpp   1/1     Running   0          100m

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/java         LoadBalancer   10.106.84.119   <pending>     8080:32014/TCP   7m50s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          5h38m
```
`minikube service --all`
```|-----------|-------------|-------------|----------------------------|
| NAMESPACE |    NAME     | TARGET PORT |            URL             |
|-----------|-------------|-------------|----------------------------|
| default   | java-spring |        8080 | http://192.168.148.2:30504 |
|-----------|-------------|-------------|----------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
```
![Screenshot from 2024-03-29 21-11-45.png](images%2FScreenshot%20from%202024-03-29%2021-11-45.png)