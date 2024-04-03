# Kubernetes

## Setup 

Firstly, we should start minikube with the docker driver

```bash
❯ minikube start -- driver=docker
😄  minikube v1.32.0 on Darwin 14.4 (arm64)
✨  Automatically selected the docker driver
📌  Using Docker Desktop driver with root privileges
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
💾  Downloading Kubernetes v1.28.3 preload ...
    > preloaded-images-k8s-v18-v1...:
🔥  Creating docker container (CPUs=2, Memory=4000MB) ...
🐳  Preparing Kubernetes v1.28.3 on Docker 24.0.7 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🔎  Verifying Kubernetes components...
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```

## Deployment and Expose 

Next we will create deployment and expose

``
```zsh
 kubectl get pods,svc
 NAME                                          READY   STATUS    RESTARTS   AGE
 pod/moscow-time-deployment-5fbbdcd688-2kbb8   1/1     Running   0          25s
 NAME             TYPE           CLUSTER-IP        EXTERNAL-IP    PORT(S)          AGE
 kubernetes       ClusterIP      192.168.194.129   <none>         443/TCP          33m
 time-in-moscow   LoadBalancer   192.168.194.179   198.19.249.2   8080:30302/TCP   3m42s
`` 
```

## Cleanup

```zsh
kubectl delete service time-in-moscow
kubectl delete deployment time-in-moscow
```