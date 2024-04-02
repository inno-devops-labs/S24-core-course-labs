# Kubernetes

## Deployment using "inconvenient way"

```bash
➜  kubectl get pods,svc
NAME                                  READY   STATUS    RESTARTS   AGE
pod/app-python-node-f797d4bc5-xm77w   1/1     Running   0          6m

NAME                      TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/app-python-node   LoadBalancer   10.108.25.45   <pending>     8080:32434/TCP   74s
service/kubernetes        ClusterIP      10.96.0.1      <none>        443/TCP          8m7s
```
## Clean up

```console
$ kubectl delete deployment,svc app-python
deployment.apps "app-python-node" deleted
service "app-python-node" deleted
```

## Deployment using declarative approach

```bash
➜  kubectl get pods,svc  
NAME                                        READY   STATUS    RESTARTS   AGE
pod/app-python-54cc978685-6jfvr             1/1     Running   0          27m
pod/app-python-54cc978685-9sgcs             1/1     Running   0          27m
pod/app-python-54cc978685-xg757             1/1     Running   0          27m
pod/app-python-deployment-9f888cb5d-6qwqn   1/1     Running   0          6s
pod/app-python-deployment-9f888cb5d-lvzbd   1/1     Running   0          6s
pod/app-python-deployment-9f888cb5d-zl69c   1/1     Running   0          6s

NAME                         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/app-python           LoadBalancer   10.108.25.45   <pending>     8080:31829/TCP   27m
service/app-python-service   LoadBalancer   10.97.109.53   <pending>     80:31322/TCP     2m23s
service/kubernetes           ClusterIP      10.96.0.1      <none>        443/TCP          84m
```

```bash
➜  minikube service --all
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python |        8080 | http://192.168.49.2:31829 |
|-----------|------------|-------------|---------------------------|
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-python-service |          80 | http://192.168.49.2:31322 |
|-----------|--------------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🏃  Starting tunnel for service app-python.
🏃  Starting tunnel for service app-python-service.
🏃  Starting tunnel for service kubernetes.
|-----------|--------------------|-------------|------------------------|
| NAMESPACE |        NAME        | TARGET PORT |          URL           |
|-----------|--------------------|-------------|------------------------|
| default   | app-python         |             | http://127.0.0.1:45311 |
| default   | app-python-service |             | http://127.0.0.1:45821 |
| default   | kubernetes         |             | http://127.0.0.1:42089 |
|-----------|--------------------|-------------|------------------------|
🎉  Opening service default/app-python in default browser...
🎉  Opening service default/app-python-service in default browser...
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
Opening in existing browser session.
Opening in existing browser session.
Opening in existing browser session.
```
![image](https://github.com/frog-da/DevOps/assets/84839431/a63d5d03-2376-4ac3-9a48-462c1f76cf0e)

## Bonus task

```bash
➜  minikube service --all
|-----------|----------------|-------------|---------------------------|
| NAMESPACE |      NAME      | TARGET PORT |            URL            |
|-----------|----------------|-------------|---------------------------|
| default   | app-go-service |        8080 | http://192.168.49.2:31721 |
|-----------|----------------|-------------|---------------------------|
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python |        8080 | http://192.168.49.2:31829 |
|-----------|------------|-------------|---------------------------|
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-python-service |          80 | http://192.168.49.2:31322 |
|-----------|--------------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🏃  Starting tunnel for service app-go-service.
🏃  Starting tunnel for service app-python.
🏃  Starting tunnel for service app-python-service.
🏃  Starting tunnel for service kubernetes.
|-----------|--------------------|-------------|------------------------|
| NAMESPACE |        NAME        | TARGET PORT |          URL           |
|-----------|--------------------|-------------|------------------------|
| default   | app-go-service     |             | http://127.0.0.1:41493 |
| default   | app-python         |             | http://127.0.0.1:45893 |
| default   | app-python-service |             | http://127.0.0.1:46109 |
| default   | kubernetes         |             | http://127.0.0.1:35481 |
|-----------|--------------------|-------------|------------------------|
🎉  Opening service default/app-go-service in default browser...
🎉  Opening service default/app-python in default browser...
🎉  Opening service default/app-python-service in default browser...
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
Opening in existing browser session.
Opening in existing browser session.
Opening in existing browser session.
Opening in existing browser session.
```
![image](https://github.com/frog-da/DevOps/assets/84839431/7d22cf1d-d454-4172-aa5c-6bde2516d16c)
