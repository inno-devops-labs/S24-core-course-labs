## Part 1

```bash
venv) smasiner@smasIners-MacBook-Pro k8s % minikube service your-app
|-----------|----------|-------------|--------------|
| NAMESPACE |   NAME   | TARGET PORT |     URL      |
|-----------|----------|-------------|--------------|
| default   | your-app |             | No node port |
|-----------|----------|-------------|--------------|
😿  service default/your-app has no node port
❗  Services [default/your-app] have type "ClusterIP" not meant to be exposed, however for local development minikube allows you to access this !
🏃  Starting tunnel for service your-app.
|-----------|----------|-------------|------------------------|
| NAMESPACE |   NAME   | TARGET PORT |          URL           |
|-----------|----------|-------------|------------------------|
| default   | your-app |             | http://127.0.0.1:57744 |
|-----------|----------|-------------|------------------------|
🎉  Opening service default/your-app in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
^C✋  Stopping tunnel for service your-app.
(venv) smasiner@smasIners-MacBook-Pro k8s % kubectl get pods,svc
NAME                            READY   STATUS    RESTARTS   AGE
pod/your-app-77c6ff4fdc-wvfcr   1/1     Running   0          17m

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP    79m
service/your-app     ClusterIP   10.109.22.230   <none>        8080/TCP   17m
```
## Part 2
Outputs
```bash
    (venv) smasiner@smasIners-MacBook-Pro k8s % kubectl get po                            
NAME                        READY   STATUS    RESTARTS   AGE
your-app-77c6ff4fdc-wvfcr   1/1     Running   0          26m
(venv) smasiner@smasIners-MacBook-Pro k8s % kubectl describe po preinstall-hook       
Error from server (NotFound): pods "preinstall-hook" not found
(venv) smasiner@smasIners-MacBook-Pro k8s % kubectl describe po postinstall-hook
Error from server (NotFound): pods "postinstall-hook" not found

```