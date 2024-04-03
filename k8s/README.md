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
NAME                              READY   STATUS             RESTARTS      AGE
pod/web-mierley-c575fb86-6l6md    1/2     CrashLoopBackOff   5 (68s ago)   4m18s
pod/web-mierley-f4675f6b7-4rvjq   1/1     Running            0             23m
pod/web-mierley-f4675f6b7-77cw5   1/1     Running            0             23m
pod/web-mierley-f4675f6b7-x66jx   1/1     Running            0             56m

NAME                          TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes            ClusterIP      10.96.0.1        <none>        443/TCP          58m
service/web-mierley           LoadBalancer   10.110.97.52     <pending>     8080:31956/TCP   48m
service/web-mierley-service   ClusterIP      10.106.213.149   <none>        81/TCP           51s
```

## `minikube service --all` output with manifest files
```
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
* service default/kubernetes has no node port
|-----------|-------------|-------------|---------------------------|
| NAMESPACE |    NAME     | TARGET PORT |            URL            |
|-----------|-------------|-------------|---------------------------|
| default   | web-mierley |        8080 | http://192.168.49.2:31956 |
|-----------|-------------|-------------|---------------------------|
|-----------|---------------------|-------------|--------------|
| NAMESPACE |        NAME         | TARGET PORT |     URL      |
|-----------|---------------------|-------------|--------------|
| default   | web-mierley-service |             | No node port |
|-----------|---------------------|-------------|--------------|
* service default/web-mierley-service has no node port
* Starting tunnel for service kubernetes.
* Starting tunnel for service web-mierley.
* Starting tunnel for service web-mierley-service.
|-----------|---------------------|-------------|------------------------|
| NAMESPACE |        NAME         | TARGET PORT |          URL           |
|-----------|---------------------|-------------|------------------------|
| default   | kubernetes          |             | http://127.0.0.1:57749 |
| default   | web-mierley         |             | http://127.0.0.1:57751 |
| default   | web-mierley-service |             | http://127.0.0.1:57753 |
|-----------|---------------------|-------------|------------------------|
```