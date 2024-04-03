# Kubernetes

## Table of Contents

- [Kubernetes](#kubernetes)
  - [Table of Contents](#table-of-contents)
  - [K8s Setup and Basic Deployment](#k8s-setup-and-basic-deployment)
  - [Declarative Kubernetes Manifests](#declarative-kubernetes-manifests)

## K8s Setup and Basic Deployment

Manual deployment was created using the following steps:

```bash
> kubectl create deployment app-python --image pptx704/app_python:latest

deployment.apps/app-python created
```

This could be verified using `get deployments`:

```bash
> kubectl get deployments

NAME         READY   UP-TO-DATE   AVAILABLE   AGE
app-python   1/1     1            1           105s
```

Now, to access the deployment, a service was created:

```bash
> kubectl expose deployment app-python --type=LoadBalancer --port=5000 --target-port=5000

service/app-python exposed
```

This could be verified using `get services` and `get pods`:

```bash
> kubectl get pods,services

NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-56d8bd6db9-x6chr   1/1     Running   0          4m51s

NAME                 TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.100.54.7   <pending>     5000:32665/TCP   74s
service/kubernetes   ClusterIP      10.96.0.1     <none>        443/TCP          32m
```

Running `minikube service app-python` would open the service in the default browser.

![Terminal](https://i.postimg.cc/GtDyT5Yn/image.png)

![Browser window](https://i.postimg.cc/Vv0NH0Lq/image.png)

To remove the created pods and services, the following commands were used:

```bash
> kubectl delete service app-python

service "app-python" deleted

> kubectl delete deployment app-python

deployment.apps "app-python" deleted
```

## Declarative Kubernetes Manifests

After creating the `yml` files for the deployment and service, I used `kubectl apply -f <filename>` to create the deployment and service.

![Manifest apply](https://i.postimg.cc/Y9vvWsgq/image.png)

Running `kubectl get pods,svc` would shows the created pods and services.

![manifest applied](https://i.postimg.cc/PqgjS39q/image.png)

Running `minikube service --all` opens the services in the default browser.

![terminal services](https://i.postimg.cc/zB7xy3C1/image.png)

Browser window for the python app-
![python app](https://i.postimg.cc/4NVBc8b5/image.png)

Browser window for the bun app-
![bun app](https://i.postimg.cc/tgt5c7mV/image.png)

