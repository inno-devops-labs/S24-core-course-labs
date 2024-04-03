# Kubernetes

## Table of Contents

- [Kubernetes](#kubernetes)
  - [Table of Contents](#table-of-contents)
  - [K8s Setup and Basic Deployment](#k8s-setup-and-basic-deployment)
  - [Declarative Kubernetes Manifests](#declarative-kubernetes-manifests)
  - [Ingress Controller](#ingress-controller)

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

This could also be verified on the dashboard by running `minikube dashboard`.

![minikube dashboard](https://i.postimg.cc/brGBDkq2/image.png)

Running `minikube service --all` opens the services in the default browser.

![terminal services](https://i.postimg.cc/zB7xy3C1/image.png)

Browser window for the python app-
![python app](https://i.postimg.cc/4NVBc8b5/image.png)

Browser window for the bun app-
![bun app](https://i.postimg.cc/tgt5c7mV/image.png)

## Ingress Controller

The ingress controller was installed and verified using the following commands:

```bash
> miniube addons enable ingress

🔎  Verifying ingress addon...
🌟  The 'ingress' addon is enabled

> kubectl get pods -n ingress-nginx

NAME                                        READY   STATUS      RESTARTS        AGE
ingress-nginx-admission-create-n6zq9        0/1     Completed   0               8m44s
ingress-nginx-admission-patch-dzbzr         0/1     Completed   1               8m44s
ingress-nginx-controller-7c6974c4d8-gbt2f   1/1     Running     1 (4m43s ago)   8m44s
```

Then the `ingress.yml` file was created and applied.

```bash
> kubectl apply -f ingress.yml

ingress.networking.k8s.io/deployment-ingress created
```

Using `minkube ip`, the IP address can be found-

![IP](https://i.postimg.cc/4NDGXNX3/image.png)

Using `curl --resolve "<app>:80:$( minikube ip )" -i http://<app>`, the app can be accessed.

![curl](https://i.postimg.cc/9fKXwthG/image.png)

To clean up, the following commands were used:

```bash
> kubectl delete -f ingress.yml

ingress.networking.k8s.io "deployment-ingress" deleted

> kubectl delete -f app_python/deployment.yml

deployment.apps "app-python-deployment" deleted

> kubectl delete -f app_bun/deployment.yml

deployment.apps "app-bun-deployment" deleted

> kubectl delete -f app_python/service.yml

service "app-python-service" deleted

> kubectl delete -f app_bun/service.yml

service "app-bun-service" deleted
```
