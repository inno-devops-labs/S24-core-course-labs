## Install Helm Chart

```console
$ helm install moscowtime-web moscowtime-web
NAME: moscowtime-web
LAST DEPLOYED: Mon Apr  8 21:04:25 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=moscowtime-web,app.kubernetes.io/instance=moscowtime-web" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

![Workloads](image-1.png)

We can see that it is deployed successfully (I'll not show the screenshot of the browser as for this assignment this is not required)
```
$ minikube service moscowtime-web
|-----------|----------------|-------------|--------------|
| NAMESPACE |      NAME      | TARGET PORT |     URL      |
|-----------|----------------|-------------|--------------|
| default   | moscowtime-web |             | No node port |
|-----------|----------------|-------------|--------------|
😿  service default/moscowtime-web has no node port
🏃  Starting tunnel for service moscowtime-web.
|-----------|----------------|-------------|------------------------|
| NAMESPACE |      NAME      | TARGET PORT |          URL           |
|-----------|----------------|-------------|------------------------|
| default   | moscowtime-web |             | http://127.0.0.1:35351 |
|-----------|----------------|-------------|------------------------|
🎉  Opening service default/moscowtime-web in default browser...
👉  http://127.0.0.1:35351
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
```

```console
$ kubectl get pods,svc
NAME                                 READY   STATUS    RESTARTS   AGE
pod/moscowtime-web-fb88cdbbb-r79z8   1/1     Running   0          8m43s

NAME                     TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/kubernetes       ClusterIP   10.96.0.1       <none>        443/TCP    5d22h
service/moscowtime-web   ClusterIP   10.109.60.194   <none>        8080/TCP   8m43s
```