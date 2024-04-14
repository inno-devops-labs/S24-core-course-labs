# Kubernetes

```
❯ kubectl get pods,svc
NAME                                READY   STATUS    RESTARTS   AGE
pod/manual-flask-64f4449c6d-cvkct   1/1     Running   0          13m

NAME                   TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes     ClusterIP      10.96.0.1        <none>        443/TCP          14m
service/manual-flask   LoadBalancer   10.103.105.146   <pending>     5000:31607/TCP   7m21s
❯ minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|--------------|-------------|---------------------------|
| NAMESPACE |     NAME     | TARGET PORT |            URL            |
|-----------|--------------|-------------|---------------------------|
| default   | manual-flask |        5000 | http://192.168.58.2:31607 |
|-----------|--------------|-------------|---------------------------|
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service manual-flask.
|-----------|--------------|-------------|------------------------|
| NAMESPACE |     NAME     | TARGET PORT |          URL           |
|-----------|--------------|-------------|------------------------|
| default   | kubernetes   |             | http://127.0.0.1:65519 |
| default   | manual-flask |             | http://127.0.0.1:65521 |
|-----------|--------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
🎉  Opening service default/manual-flask in default browser...
```

### Delete deployment and service
```
❯ kubectl delete services manual-flask
service "manual-flask" deleted
❯ kubectl delete deployment manual-flask
deployment.apps "manual-flask" deleted
```


### Screenshots

![](/S24-core-course-labs/k8s/images/getpods.png)
![](/S24-core-course-labs/k8s/images/services.png)
![](/S24-core-course-labs/k8s/images/app.png)