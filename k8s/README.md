# Kubernetes Resources

This folder contains Kubernetes manifests for deploying our application.

## Pods

```bash
kubectl get pods
```

```bash
NAME                             READY   STATUS             RESTARTS   AGE
my-app-devops-6f759f666f-7wf6s   1/1     Running            0          37m
```


## Services

```bash
kubectl get svc
```

```bash
NAME            TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
kubernetes      ClusterIP   10.96.0.1      <none>        443/TCP          50m
my-app-devops   NodePort    10.98.62.223   <none>        5000:31230/TCP   7m33s
```


##Declarative Kubernetes Manifests
```bash
(venv) (base) dilaraf@MacBook-Air app_python % minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🏃  Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:57359 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.


```

![k8s screenshots](img.png)
![k8s screenshots](img_1.png)