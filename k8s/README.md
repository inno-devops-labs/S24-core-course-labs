# Deploy

![](./assets/setup.png)

# Access

![](./assets/access.png)

# Result of command

```text
NAME                                      READY   STATUS    RESTARTS   AGE
pod/moscow-python-time-7d6dc4568c-fkghl   1/1     Running   0          36s

NAME                         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP    45m
service/moscow-python-time   ClusterIP   10.96.231.123   <none>        5000/TCP   29s
```

# Clean up

![](./assets/delete.png)

# 2nd result of command

```text
NAME                                      READY   STATUS    RESTARTS   AGE
pod/moscow-python-time-6c4478fc97-88jm8   1/1     Running   0          20s
pod/moscow-python-time-6c4478fc97-pzftx   1/1     Running   0          20s
pod/moscow-python-time-6c4478fc97-s998n   1/1     Running   0          20s

NAME                                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/kubernetes                   ClusterIP      10.96.0.1       <none>        443/TCP        52m
service/moscow-python-time-service   LoadBalancer   10.105.63.171   <pending>     80:31687/TCP   16s
```

# minikube service --all

```text
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|----------------------------|-------------|---------------------------|
| NAMESPACE |            NAME            | TARGET PORT |            URL            |
|-----------|----------------------------|-------------|---------------------------|
| default   | moscow-python-time-service |          80 | http://192.168.49.2:31687 |
|-----------|----------------------------|-------------|---------------------------|
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service moscow-python-time-service.
|-----------|----------------------------|-------------|------------------------|
| NAMESPACE |            NAME            | TARGET PORT |          URL           |
|-----------|----------------------------|-------------|------------------------|
| default   | kubernetes                 |             | http://127.0.0.1:53814 |
| default   | moscow-python-time-service |             | http://127.0.0.1:53817 |
|-----------|----------------------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
🎉  Opening service default/moscow-python-time-service in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```

Same port
![](./assets/access2.png)


# Bonus 

`kubectl get pods,svc`

```text
NAME                                              READY   STATUS    RESTARTS   AGE
pod/moscow-python-time-64959bfb5-bj5zv        1/1     Running   0          39s
pod/moscow-python-time-64959bfb5-brhtr        1/1     Running   0          39s
pod/moscow-python-time-64959bfb5-q77qq        1/1     Running   0          39s
pod/moscow-flutter-time-568b54759c-dsw9q   1/1     Running   0          44s
pod/moscow-flutter-time-568b54759c-jcbcs   1/1     Running   0          44s
pod/moscow-flutter-time-568b54759c-rm2f4   1/1     Running   0          44s
NAME                                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes                   ClusterIP      10.96.0.1        <none>        443/TCP          7d1h
service/moscow-python-time-service     LoadBalancer   10.111.152.135   <pending>     5000:32194/TCP   39s
service/moscow-flutter-time-service   LoadBalancer   10.98.251.93     <pending>     80:31420/TCP   44s
```

`minikube service --all`
```text
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|----------------------------|-------------|---------------------------|
| NAMESPACE |          NAME              | TARGET PORT |            URL            |
|-----------|----------------------------|-------------|---------------------------|
| default   | moscow-python-time-service |        5000 | http://192.168.49.2:30974 |
|-----------|----------------------------|-------------|---------------------------|
|-----------|----------------------------|-------------|---------------------------|
| NAMESPACE |            NAME            | TARGET PORT |            URL            |
|-----------|----------------------------|-------------|---------------------------|
| default   | moscow-flutter-time-service|        80 | http://192.168.49.2:31731 |
|-----------|----------------------------|-------------|---------------------------|
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service moscow-time-service-go.
🏃  Starting tunnel for service moscow-time-service-python.
|-----------|----------------------------|-------------|------------------------|
| NAMESPACE |            NAME            | TARGET PORT |          URL           |
|-----------|----------------------------|-------------|------------------------|
| default   | kubernetes                 |             | http://127.0.0.1:59561 |
| default   | moscow-time-service-go     |             | http://127.0.0.1:59563 |
| default   | moscow-time-service-python |             | http://127.0.0.1:59565 |
|-----------|----------------------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
🎉  Opening service default/moscow-time-service-go in default browser...
🎉  Opening service default/moscow-time-service-python in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```


### Flutter

![](./assets/flutter.png)

### Python

![](./assets/python.png)
