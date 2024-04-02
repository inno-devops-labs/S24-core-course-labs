# Kubernetes

## Setup

Let's use `docker` driver for `minikube start`:

```bash
i-pechersky@i-pechersky-x S24-core-course-labs % minikube start --driver=docker
🔥  Deleting "minikube" in kvm2 ...
💀  Removed all traces of the "minikube" cluster.
 dmfrpro@dmfrpro-pc  ~  minikube start --driver=docker
😄  minikube v1.32.0 on Arch rolling
✨  Using the docker driver based on user configuration
📌  Using Docker driver with root privileges
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
    > gcr.io/k8s-minikube/kicbase...:  453.90 MiB / 453.90 MiB  100.00% 32.63 M
🔥  Creating docker container (CPUs=2, Memory=3900MB) ...
🐳  Preparing Kubernetes v1.28.3 on Docker 24.0.7 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```

## Deployment

Create a deployment and expose:

```bash
i-pechersky@i-pechersky-x S24-core-course-labs % kubectl create deployment app_python --image=happystove/app_python
deployment.apps/app_python created

i-pechersky@i-pechersky-x S24-core-course-labs % kubectl expose deployment app_python --type=LoadBalancer --port=8080
service/app_python exposed

i-pechersky@i-pechersky-x S24-core-course-labs % kubectl get pods,svc
NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)          AGE
service/app_python   LoadBalancer   10.103.210.16   10.103.210.16   8080:30752/TCP   30s
service/kubernetes   ClusterIP      10.96.0.1       <none>          443/TCP          6m5s

NAME                              READY   STATUS    RESTARTS   AGE
pod/app_python-6d7d4dc689-hbjbh   1/1     Running   0          38s
```

Verify availability:

```bash
$ curl 10.103.210.16:8080
<!DOCTYPE html>
<html>
<head>
    <title>Current Time in Moscow</title>
</head>
<body>
    <h1>Current Time in Moscow:</h1>
    <p>2024-04-02 21:35:22.065365+03:00</p>
</body>
```

Cleanup

```bash
i-pechersky@i-pechersky-x S24-core-course-labs % kubectl delete deployment app_python
deployment.apps "app_python" deleted

i-pechersky@i-pechersky-x S24-core-course-labs % kubectl delete service app_python
service "app_python" deleted

i-pechersky@i-pechersky-x S24-core-course-labs % kubectl get svc,pods
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   7m21s
```

## Use deployment and service manifests

```bash
i-pechersky@i-pechersky-x S24-core-course-labs % cd k8s
/Users/i-pechersky/DevOps/S24-core-course-labs/k8s

i-pechersky@i-pechersky-x k8s % kubectl apply -f app_python
deployment.apps/app_python created
service/app_python created

i-pechersky@i-pechersky-x k8s % kubectl get svc,pods
NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)          AGE
service/app_python   LoadBalancer   10.108.0.193    10.108.0.193    8080:30334/TCP   74s
service/kubernetes   ClusterIP      10.96.0.1       <none>          443/TCP          13m

NAME                              READY   STATUS    RESTARTS   AGE
pod/app_python-69fffb44c4-5pgmv   1/1     Running   0          74s
pod/app_python-69fffb44c4-bfwkl   1/1     Running   0          74s
pod/app_python-69fffb44c4-xmx6j   1/1     Running   0          9s
```

Output of `minikube tunnel` in a separate tab:

```bash
Status:
        machine: minikube
        pid: 63320
        route: 10.96.0.0/12 -> 192.168.49.2
        minikube: Running
        services: [app_python]
    errors: 
                minikube: no errors
                router: no errors
                loadbalancer emulator: no errors
```

```bash
i-pechersky@i-pechersky-x k8s % minikube service --all
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app_python |        8080 | http://192.168.49.2:30334 |
|-----------|------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🎉  Opening service default/app_python in default browser...
```

Availability:

```bash
i-pechersky@i-pechersky-x k8s % curl http://192.168.49.2:30334
<!DOCTYPE html>
<html>
<head>
    <title>Current Time in Moscow</title>
</head>
<body>
    <h1>Current Time in Moscow:</h1>
    <p>2024-04-02 22:47:23.124236+03:00</p>
</body>
```

## Ingress

Enable ingress addon:

```bash
i-pechersky@i-pechersky-x k8s % minikude addons enable ingress
💡  ingress is an addon maintained by Kubernetes. For any concerns contact minikube on GitHub.
You can view the list of minikube maintainers at: https://github.com/kubernetes/minikube/blob/master/OWNERS
    ▪ Using image registry.k8s.io/ingress-nginx/controller:v1.9.4
    ▪ Using image registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20231011-8b53cabe0
    ▪ Using image registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20231011-8b53cabe0
🔎  Verifying ingress addon...
🌟  The 'ingress' addon is enabled
```

Apply ingress:

```bash
i-pechersky@i-pechersky-x k8s % kubectl apply -f ingress.yml
ingress.networking.k8s.io/example-ingress created

i-pechersky@i-pechersky-x k8s % kubectl get all -n ingress-nginx
NAME                                            READY   STATUS      RESTARTS   AGE
pod/ingress-nginx-admission-create-8mfgz        0/1     Completed   0          95m
pod/ingress-nginx-admission-patch-4thks         0/1     Completed   0          95m
pod/ingress-nginx-controller-7c6974c4d8-5qmrp   1/1     Running     0          95m

NAME                                         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)                      AGE
service/ingress-nginx-controller             NodePort    10.110.203.1   <none>        80:32744/TCP,443:30263/TCP   95m
service/ingress-nginx-controller-admission   ClusterIP   10.109.41.64   <none>        443/TCP                      95m

NAME                                       READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/ingress-nginx-controller   1/1     1            1           95m

NAME                                                  DESIRED   CURRENT   READY   AGE
replicaset.apps/ingress-nginx-controller-7c6974c4d8   1         1         1       95m

NAME                                       COMPLETIONS   DURATION   AGE
job.batch/ingress-nginx-admission-create   1/1           14s        95m
job.batch/ingress-nginx-admission-patch    1/1           14s        95m

i-pechersky@i-pechersky-x k8s % minikube service --all -n ingress-nginx
|---------------|--------------------------|-------------|---------------------------|
|   NAMESPACE   |           NAME           | TARGET PORT |            URL            |
|---------------|--------------------------|-------------|---------------------------|
| ingress-nginx | ingress-nginx-controller | http/80     | http://192.168.49.2:32744 |
|               |                          | https/443   | http://192.168.49.2:30263 |
|---------------|--------------------------|-------------|---------------------------|
|---------------|------------------------------------|-------------|--------------|
|   NAMESPACE   |                NAME                | TARGET PORT |     URL      |
|---------------|------------------------------------|-------------|--------------|
| ingress-nginx | ingress-nginx-controller-admission |             | No node port |
|---------------|------------------------------------|-------------|--------------|
😿  service ingress-nginx/ingress-nginx-controller-admission has no node port
[ingress-nginx ingress-nginx-controller http/80
https/443 http://192.168.49.2:32744
http://192.168.49.2:30263]
```

Availability:

```bash
i-pechersky@i-pechersky-x k8s % curl --resolve "pechersky.python.app:80:$(minikube ip)" -i pechersky.python.app
HTTP/1.1 200 OK
Date: Mon, 02 Apr 2024 21:48:17 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 183
Connection: keep-alive

<!DOCTYPE html>
<html>
<head>
    <title>Current Time in Moscow</title>
</head>
<body>
    <h1>Current Time in Moscow:</h1>
    <p>2024-04-01 21:48:17.178496+03:00</p>
</body>
```
