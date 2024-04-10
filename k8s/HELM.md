## Creating a Helm Chart
We will be creating a HELM chart for our python application using the following command:
```bash
helm create app-python
```

This will create a directory structure for our helm chart. The directory structure will look like this:
```bash
app-python/
  Chart.yaml
  values.yaml
  charts/
  templates/
  templates/NOTES.txt
  templates/_helpers.tpl
  templates/deployment.yaml
  templates/ingress.yaml
  templates/service.yaml
  templates/tests/
  templates/tests/test-connection.yaml
  templates/tests/test-connection.yaml
```

The `Chart.yaml` file contains the metadata for the chart. The `values.yaml` file contains the default values for the chart. The `templates` directory contains the templates for the Kubernetes resources that will be created by the chart.

## Deploying the Helm Chart
To deploy the helm chart, we will use the following command:
```bash
helm install app-python ./app-python
```

To make sure that the deployment was successful, we will check the output of `kubectl get pods` and `kubectl get svc` commands.

```
$ kubectl get pods

NAME                          READY   STATUS    RESTARTS   AGE
app-python-57d59698db-bqqdq   1/1     Running   0          43s

$ kubectl get svc

NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
app-python   ClusterIP   10.106.0.152   <none>        80/TCP    71s
kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP   30m
```


## Using Hooks in Helm Charts
Hooks in Helm charts are used to perform actions at different points in the lifecycle of a release. There are different types of hooks that can be used in Helm charts, such as pre-install, post-install, pre-delete, and post-delete hooks.

We will be using pre-install and post-install hooks in our Helm chart. The configuration for the hooks will be added inside the `templates` directory.

We are using a delete policy `hook-succeeded` for the hooks. This policy tells helm to automatically delete the hook pod after it has completed successfully. 

### Output of the commands
```
$ kubectl get po

app-python-57d59698db-tslpp   1/1     Running     0          2m40s
postinstall-hook              0/1     Completed   0          2m40s
preinstall-hook               0/1     Completed   0          3m2s

$ kubectl describe po preinstall-hook

Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.58.2
Start Time:       Wed, 10 Apr 2024 09:01:24 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.8
IPs:
  IP:  10.244.0.8
Containers:
  pre-install-container:
    Container ID:  docker://bf32fdb378c819ff767b83ff0807648a930c7b4db7601b6dd00ae4a2d0505e0c
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
      Started:      Wed, 10 Apr 2024 09:01:25 +0300
      Finished:     Wed, 10 Apr 2024 09:01:45 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-54p2c (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-54p2c:
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
  Normal  Scheduled  3m46s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     3m46s  kubelet            Container image "busybox" already present on machine
  Normal  Created    3m46s  kubelet            Created container pre-install-container
  Normal  Started    3m45s  kubelet            Started container pre-install-container


$ kubectl describe po postinstall-hook

Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.58.2
Start Time:       Wed, 10 Apr 2024 09:01:46 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.10
IPs:
  IP:  10.244.0.10
Containers:
  post-install-container:
    Container ID:  docker://864533b6b7163bf879c110f79fd1a30b0add93c5aecc2506c2219c2947f1a21c
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 10 Apr 2024 09:01:49 +0300
      Finished:     Wed, 10 Apr 2024 09:02:09 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-94xkv (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-94xkv:
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
  Normal  Scheduled  4m15s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    4m14s  kubelet            Pulling image "busybox"
  Normal  Pulled     4m12s  kubelet            Successfully pulled image "busybox" in 1.781s (1.781s including waiting)
  Normal  Created    4m12s  kubelet            Created container post-install-container
  Normal  Started    4m12s  kubelet            Started container post-install-container
```

## Bonus Task

### Using Helm for the Extra App
We will be using the following commands to create a helm chart for the extra app:
```bash
helm create app-javascript
helm install app-javascript ./app-javascript
```

To make sure that the deployment was successful, we will check the output of `kubectl get pods` and `kubectl get svc` commands.

```
$ kubectl get pods

NAME                              READY   STATUS      RESTARTS   AGE
app-javascript-589dc7f5dd-j8zs5   1/1     Running     0          6s
app-python-57d59698db-tslpp       1/1     Running     0          15m

$ kubectl get svc

NAME             TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
app-javascript   ClusterIP   10.98.233.140    <none>        80/TCP    2m17s
app-python       ClusterIP   10.107.134.115   <none>        80/TCP    17m
kubernetes       ClusterIP   10.96.0.1        <none>        443/TCP   68m
```

### Library Charts
Library charts are used to define reusable components that can be used across multiple charts. We have created charts for the python and javascript applications and installed them.

To verify that the library charts are working correctly, we will check the output of the `kubectl get pods` and `kubectl get svc` commands.

```
$ kubectl get pods

NAME                                      READY   STATUS              RESTARTS   AGE
app-javascript-589dc7f5dd-j8zs5           1/1     Running             0          12m
app-javascript-library-84cd5bf77d-mgkc8   1/1     Running             0          3s
app-python-57d59698db-tslpp               1/1     Running             0          27m
app-python-library-58b4c6fd75-lj99w       1/1     Running             0          48s

$ kubectl get svc

NAME                     TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
app-javascript           ClusterIP   10.98.233.140    <none>        80/TCP    14m
app-javascript-library   ClusterIP   10.108.235.19    <none>        80/TCP    73s
app-python               ClusterIP   10.107.134.115   <none>        80/TCP    28m
app-python-library       ClusterIP   10.98.89.55      <none>        80/TCP    118s
kubernetes               ClusterIP   10.96.0.1        <none>        443/TCP   80m
```