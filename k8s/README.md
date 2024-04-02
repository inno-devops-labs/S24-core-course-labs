## Kubernetes configuration

```bash
$minicube start 
```

1. **Create deployment**
```bash
$cubectl create deployment app-python --image=vikono/devops:latest
deployment.apps/app-python created
```

2. **Access to application**
```bash
$kubectl expose deployment app-python --type=LoadBalancer --port=8000
service/app-python exposed
```

3. **Run command to see pods and services**
```bash
$kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-69dd5cf769-d62g5   1/1     Running   0          9m48s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.105.45.158   <pending>     8000:31950/TCP   72s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          10m
```

4. **Cleanup**
```bash
$kubectl delete deployment app-python
deployment.apps "app-python" deleted

$kubectl delete service app-python
service "app-python" deleted
```

5. **Declarative K8s Manifests**
```bash
$cd k8s
$kubectl apply -f .
deployment.apps/app-python-deployment created
service/app-python-deployment created
```

**See pods and services**
```bash
$kubectl get pods,svc
NAME                                         READY   STATUS    RESTARTS   AGE
pod/app-python-deployment-5fbfc9c847-5zm74   1/1     Running   0          117s
pod/app-python-deployment-5fbfc9c847-6zz9x   1/1     Running   0          117s
pod/app-python-deployment-5fbfc9c847-v56t5   1/1     Running   0          117s

NAME                            TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python-deployment   LoadBalancer   10.111.66.131   <pending>     8000:31343/TCP   117s
service/kubernetes              ClusterIP      10.96.0.1       <none>        443/TCP          39m
```

```bash
$minikube service --all
|-----------|-----------------------|-------------|---------------------------|
| NAMESPACE |         NAME          | TARGET PORT |            URL            |
|-----------|-----------------------|-------------|---------------------------|
| default   | app-python-deployment |        8000 | http://192.168.49.2:31704 |
|-----------|-----------------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🎉  Opening service default/app-python-deployment in default browser...
```
