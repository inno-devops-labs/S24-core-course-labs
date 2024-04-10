# HELM

## Table of contents

- [HELM](#helm)
  - [Table of contents](#table-of-contents)
  - [Creating a Helm chart for the Python app](#creating-a-helm-chart-for-the-python-app)
  - [Linting and Dry Running](#linting-and-dry-running)
  - [`describe`ing preinstall-hook and postinstall-hook](#describeing-preinstall-hook-and-postinstall-hook)
  - [Adding delete policy](#adding-delete-policy)
  - [Chart for Secondary App](#chart-for-secondary-app)
  - [Library chart](#library-chart)

## Creating a Helm chart for the Python app

After installing Helm and adding bitnami repository, I created a template Helm chart for the Python app using `helm create app-python` command.

Afterwards, I modified the `values.yaml` file to change service type to `LoadBalancer` and changed the port to `5000`. (The assignment instruction mentions changing `deployment.yaml` for this but apparently that's what the `values.yaml` file is for.)

After that, I ran the `helm install` command to deploy the Python app.

```bash
> helm install app-python app-python

NAME: app-python
LAST DEPLOYED: Wed Apr 10 07:16:08 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get --namespace default svc -w app-python'
  export SERVICE_IP=$(kubectl get svc --namespace default app-python --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:5000
```

The service was created successfully and I was able to access the Python app using the external IP address.

![Minikube Service](https://i.postimg.cc/C1kFJ12M/image.png)

```bash
> curl http://192.168.49.2:31450


<h1>Current time in Moscow: 10:24 (10:24 AM)</h1>
```

This can be checked by using `kubectl get` command also.

![kubectl get pod,svc](https://i.postimg.cc/5N7MBLtq/image.png)

## Linting and Dry Running

Using `helm lint`, I checked the Helm chart for any syntax errors.

```bash
> helm lint app-python/
==> Linting app-python/

1 chart(s) linted, 0 chart(s) failed
```

Using `helm install --dry-run`, I checked the Helm chart for any errors.

```bash
> helm install --dry-run helm-hooks app-python

NAME: helm-hooks
LAST DEPLOYED: Wed Apr 10 08:16:14 2024
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: app-python/templates/post-install-hook.yml
apiVersion: v2
kind: Pod
metadata:
   name: postinstall-hook
   annotations:
       "helm.sh/hook": "post-install"
spec:
  containers:
  - name: post-install-container
    image: busybox
    imagePullPolicy: Always
    command: ['sh', '-c', 'echo The post-install hook is running && sleep 15' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---
# Source: app-python/templates/pre-install-hook.yml
apiVersion: v2
kind: Pod
metadata:
   name: preinstall-hook
   annotations:
       "helm.sh/hook": "pre-install"
spec:
  containers:
  - name: pre-install-container
    image: busybox
    imagePullPolicy: IfNotPresent
    command: ['sh', '-c', 'echo The pre-install hook is running && sleep 20' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0

...
```

## `describe`ing preinstall-hook and postinstall-hook

The following was used for preinstall-hook and postinstall-hook before adding any delete policy.

Using `kubectl get po` command, I checked the status of the pods.

![kubectl get po](https://i.postimg.cc/XY6HRvXB/image.png)

```bash

> kubectl describe pod preinstall-hook

Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 08:22:40 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.16
IPs:
  IP:  10.244.0.16
Containers:
  pre-install-container:
    Container ID:  docker://c2f284c39d3a1a0dd4c970164b347ab5f4d9ece98d9d77221888b806e0e4aa0c
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 10 Apr 2024 08:22:50 +0300
      Finished:     Wed, 10 Apr 2024 08:23:10 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-pxx7n (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-pxx7n:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  2m7s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    2m5s  kubelet            Pulling image "busybox"
  Normal  Pulled     118s  kubelet            Successfully pulled image "busybox" in 7.296s (7.296s including waiting)
  Normal  Created    117s  kubelet            Created container pre-install-container
  Normal  Started    117s  kubelet            Started container pre-install-container
```

```bash
> kubectl describe pod postinstall-hook

Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 08:23:13 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.18
IPs:
  IP:  10.244.0.18
Containers:
  post-install-container:
    Container ID:  docker://f51c906cdccb88608dabf4c08b6d061ffec4c9dc5ced420db68b92e7be46c01f
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 15
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 10 Apr 2024 08:23:17 +0300
      Finished:     Wed, 10 Apr 2024 08:23:32 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-9d7dg (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-9d7dg:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  2m18s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    2m17s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m15s  kubelet            Successfully pulled image "busybox" in 1.91s (1.912s including waiting)
  Normal  Created    2m15s  kubelet            Created container post-install-container
  Normal  Started    2m15s  kubelet            Started container post-install-container
```

## Adding delete policy

In the `post-install-hook` and `pre-install-hook`, I added `"helm.sh/hook-delete-policy": hook-succeeded` annotation to delete the pods after the hooks have run successfully.

When I run the `helm install` command, the pods are deleted after the hooks have run successfully.

In the screenshot below, it can be seen that `preinstall-hook` is deleted and only application pod and `postinstall-hook` are running. postinstall-hook is also deleted after it finishes running.

![Delete hook policy](https://i.postimg.cc/mrD3ccrn/image.png)

## Chart for Secondary App

The same procedures were followed for the `app_bun` application.

![Bun app](https://i.postimg.cc/htrHk806/image.png)

## Library chart

I created a library chart that contains some common boilerplate code for the Python app and the Bun app.

Afterward, dependencies were added inside `Chart.yaml` file and `helm dependency update` command was run.

![Library chart apply](https://i.postimg.cc/Jtw21NcZ/image.png)

Running `helm install` command for the library chart was successful.

![Library chart run](https://i.postimg.cc/HL2Km8hP/image.png)

Afterwards `minikube service` and `kubectl get svc` commands were run to start and check the services.

![Library chart working](https://i.postimg.cc/W3p4prbD/image.png)
