# K8S

## Simple deployment

```
atm1nd@fatm1nd-IdeaPad-5-14ARE05:/tmp$ minikube start --driver=docker
😄  minikube v1.32.0 on Ubuntu 22.04
✨  Using the docker driver based on user configuration
📌  Using Docker driver with root privileges
❗  For an improved experience it's recommended to use Docker Engine instead of Docker Desktop.
Docker Engine installation instructions: https://docs.docker.com/engine/install/#server
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
    > gcr.io/k8s-minikube/kicbase...:  453.90 MiB / 453.90 MiB  100.00% 4.94 Mi
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
🐳  Preparing Kubernetes v1.28.3 on Docker 24.0.7 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🔎  Verifying Kubernetes components...
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:/tmp$ kubectl create deployment web-app --image=docker.io/fatm1nd/devops-lab-container:latest --port=5000
deployment.apps/web-app created
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:/tmp$ kubectl get deployments
NAME      READY   UP-TO-DATE   AVAILABLE   AGE
web-app   1/1     1            1           29s
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:/tmp$ kubectl get svc
NAME         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          3m52s
web-app      LoadBalancer   10.103.161.247   <pending>     8080:30542/TCP   7s
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:/tmp$ kubectl get pods
NAME                       READY   STATUS    RESTARTS   AGE
web-app-5db4bdd7cf-tkf9m   1/1     Running   0          20m
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:/tmp$ minikube service web-app
|-----------|---------|-------------|---------------------------|
| NAMESPACE |  NAME   | TARGET PORT |            URL            |
|-----------|---------|-------------|---------------------------|
| default   | web-app |        8080 | http://192.168.49.2:32171 |
|-----------|---------|-------------|---------------------------|
🏃  Starting tunnel for service web-app.
|-----------|---------|-------------|------------------------|
| NAMESPACE |  NAME   | TARGET PORT |          URL           |
|-----------|---------|-------------|------------------------|
| default   | web-app |             | http://127.0.0.1:46277 |
|-----------|---------|-------------|------------------------|
🎉  Opening service default/web-app in default browser...
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
Found ffmpeg: /opt/yandex/browser-beta/libffmpeg.so
	avcodec: 3882340
	avformat: 3876196
	avutil: 3746916
FFmpeg version is too old. Need:
	avcodec: 3939428
	avformat: 3935844
	avutil: 3808100
find_ffmpeg failed, using the integrated library.
Opening in existing browser session.
```

## Use Manifests

```
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course$ kubectl get pods,svc
NAME                                      READY   STATUS    RESTARTS   AGE
pod/web-app-deployment-856645cfdd-7ccdb   1/1     Running   0          11m

NAME                      TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
service/kubernetes        ClusterIP   10.96.0.1     <none>        443/TCP          25h
service/web-app-service   NodePort    10.99.1.159   <none>        8080:30007/TCP   10m
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course$ minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|-----------------|-------------|---------------------------|
| NAMESPACE |      NAME       | TARGET PORT |            URL            |
|-----------|-----------------|-------------|---------------------------|
| default   | web-app-service |        8080 | http://192.168.49.2:30007 |
|-----------|-----------------|-------------|---------------------------|
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service web-app-service.
|-----------|-----------------|-------------|------------------------|
| NAMESPACE |      NAME       | TARGET PORT |          URL           |
|-----------|-----------------|-------------|------------------------|
| default   | kubernetes      |             | http://127.0.0.1:34077 |
| default   | web-app-service |             | http://127.0.0.1:40767 |
|-----------|-----------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
/snap/core20/current/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.29' not found (required by /lib/x86_64-linux-gnu/libproxy.so.1)
Failed to load module: /home/fatm1nd/snap/code/common/.cache/gio-modules/libgiolibproxy.so
🎉  Opening service default/web-app-service in default browser...
Found ffmpeg: /opt/yandex/browser-beta/libffmpeg.so
        avcodec: 3882340
        avformat: 3876196
        avutil: 3746916
FFmpeg version is too old. Need:
        avcodec: 3939428
        avformat: 3935844
        avutil: 3808100
find_ffmpeg failed, using the integrated library.
/snap/core20/current/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.29' not found (required by /lib/x86_64-linux-gnu/libproxy.so.1)
Failed to load module: /home/fatm1nd/snap/code/common/.cache/gio-modules/libgiolibproxy.so
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
Found ffmpeg: /opt/yandex/browser-beta/libffmpeg.so
        avcodec: 3882340
        avformat: 3876196
        avutil: 3746916
FFmpeg version is too old. Need:
        avcodec: 3939428
        avformat: 3935844
        avutil: 3808100
find_ffmpeg failed, using the integrated library.
Opening in existing browser session.
Opening in existing browser session.
```

## Screenshots

![scrrenshot](./assets/image.png)
