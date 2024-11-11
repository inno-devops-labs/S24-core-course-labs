# Kubernetes lab

## Command output

### kubectl get pods,svc

```
NAME                               READY   STATUS    RESTARTS   AGE
pod/time-server-58c57f6d45-4m4wd   1/1     Running   0          3m34s
pod/time-server-58c57f6d45-8f8w9   1/1     Running   0          112s
pod/time-server-58c57f6d45-hfdzz   1/1     Running   0          3m34s

NAME                  TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes    ClusterIP      10.96.0.1      <none>        443/TCP          5m7s
service/time-server   LoadBalancer   10.99.218.30   127.0.0.1     5000:30382/TCP   3m31s
```

### kubectl service --all

Note that this is the output for Windows/WSL2 environment.

```
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|-------------|-------------|---------------------------|
| NAMESPACE |    NAME     | TARGET PORT |            URL            |
|-----------|-------------|-------------|---------------------------|
| default   | time-server |        5000 | http://192.168.49.2:30382 |
|-----------|-------------|-------------|---------------------------|
❗  Services [default/kubernetes] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service time-server.
|-----------|-------------|-------------|------------------------|
| NAMESPACE |    NAME     | TARGET PORT |          URL           |
|-----------|-------------|-------------|------------------------|
| default   | kubernetes  |             | http://127.0.0.1:46502 |
| default   | time-server |             | http://127.0.0.1:44982 |
|-----------|-------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
👉  http://127.0.0.1:46502
🎉  Opening service default/time-server in default browser...
👉  http://127.0.0.1:44982
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
```

### App deployment

![image](https://github.com/user-attachments/assets/a0b7559f-7183-43ec-8370-02a59726a931)
