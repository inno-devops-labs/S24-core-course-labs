# K8S lab 9

## Output of commands

- `kubectl get pods,svc`

```bash
NAME                            READY   STATUS    RESTARTS   AGE
pod/app-python-f547f676-567wb   1/1     Running   0          4m59s
pod/app-python-f547f676-mtmdv   1/1     Running   0          4m59s
pod/app-python-f547f676-t6l8n   1/1     Running   0          4m59s

NAME                 TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.101.8.72   <pending>     5000:32394/TCP   103s
service/kubernetes   ClusterIP      10.96.0.1     <none>        443/TCP          7m29s
```

- `minikube service --all`

```bash
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python |        5000 | http://192.168.49.2:32394 |
|-----------|------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🎉  Opening service default/app-python in default browser...
🏃  Starting tunnel for service kubernetes.
Opening in existing browser session.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:38439 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
```

## Testing

- From browser:

![image1](1.png)

- Using curl:

```bash
$ curl http://192.168.49.2:32394/
{"time":"2024:09:01 16:22:50 MSK +0300"}
```
