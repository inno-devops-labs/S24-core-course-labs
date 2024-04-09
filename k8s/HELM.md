# HELM
## Helm Setup and Chart Creation
following commands to create the chart for the app-python and bonus app: 
```shell
minikube start --driver=docker
helm install app-python app-python/ --values app-python/values.yaml
```

## Output of the command kubectl get pods,svc

```bash
NAME                                  READY   STATUS    RESTARTS   AGE
pod/app-python-c5657fb4d-wkwz6        1/1     Running   0          3m21s

NAME                      TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/kubernetes        ClusterIP   10.96.0.1       <none>        443/TCP        6d23h
service/app-python        NodePort    10.102.33.229   <none>        5000:31085/TCP   3m21s
```

## Output of the command kubectl get po

```bash
NAME                              READY   STATUS      RESTARTS      AGE
app-python-c5657fb4d-zv529        1/1     Running     0             54s
post-install-hook                 0/1     Completed   1 (29s ago)   54s
pre-install-hook                  0/1     Completed   1 (31s ago)   54s
```

## Output of the command kubectl describe po pre-install-hook

```bash
Name:             pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Mon, 08 Apr 2024 11:45:31 +0300
Labels:           app.kubernetes.io/managed-by=Helm
Annotations:      meta.helm.sh/release-name: app-python
                  meta.helm.sh/release-namespace: default
Status:           Running
IP:               10.244.0.24
IPs:
  IP:  10.244.0.24
Containers:
  pre-install-container:
    Container ID:  docker://249a3abdb5b00f252fe46b9c9db2ad2753490ebe9a65fa2616b5a7e6a666d5ce
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Args:
      sleep
      20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Mon, 08 Apr 2024 11:47:21 +0300
      Finished:     Mon, 08 Apr 2024 11:47:41 +0300
    Last State:     Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Mon, 08 Apr 2024 11:46:33 +0300
      Finished:     Mon, 08 Apr 2024 11:46:53 +0300
    Ready:          False
    Restart Count:  3
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-d7t7p (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-d7t7p:
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
  Type     Reason     Age                  From               Message
  ----     ------     ----                 ----               -------
  Normal   Scheduled  2m11s                default-scheduler  Successfully assigned default/pre-install-hook to minikube
  Normal   Pulled     2m9s                 kubelet            Successfully pulled image "busybox" in 1.884s (1.884s including waiting)
  Normal   Pulled     106s                 kubelet            Successfully pulled image "busybox" in 1.762s (1.762s including waiting)
  Normal   Pulled     70s                  kubelet            Successfully pulled image "busybox" in 2.024s (2.024s including waiting)
  Normal   Pulling    24s (x4 over 2m11s)  kubelet            Pulling image "busybox"
  Normal   Created    22s (x4 over 2m9s)   kubelet            Created container pre-install-container
  Normal   Started    22s (x4 over 2m9s)   kubelet            Started container pre-install-container
  Normal   Pulled     22s                  kubelet            Successfully pulled image "busybox" in 2.005s (2.005s including waiting)
  Warning  BackOff    2s (x4 over 86s)     kubelet            Back-off restarting failed container pre-install-container in pod pre-install-hook_default(616e2003-375c-4721-850f-51ff8c6665f6)
```

## Output of the command kubectl describe po post-install-hook

```bash
Name:             post-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Mon, 08 Apr 2024 11:49:31 +0300
Labels:           app.kubernetes.io/managed-by=Helm
Annotations:      meta.helm.sh/release-name: app-python
                  meta.helm.sh/release-namespace: default
Status:           Running
IP:               10.244.0.25
IPs:
  IP:  10.244.0.25
Containers:
  post-install-container:
    Container ID:  docker://edf4a503c6ac841587393cc236edaadf2179d2dd9bc48c057395e16327dac11c
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Args:
      sleep
      20
    State:          Running
      Started:      Mon, 08 Apr 2024 11:51:26 +0300
    Last State:     Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Mon, 08 Apr 2024 11:50:36 +0300
      Finished:     Mon, 08 Apr 2024 11:50:56 +0300
    Ready:          True
    Restart Count:  3
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-n56kt (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  kube-api-access-n56kt:
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
  Type     Reason     Age                  From               Message
  ----     ------     ----                 ----               -------
  Normal   Scheduled  2m14s                default-scheduler  Successfully assigned default/post-install-hook to minikube
  Normal   Pulled     2m11s                kubelet            Successfully pulled image "busybox" in 1.636s (3.51s including waiting)
  Normal   Pulled     107s                 kubelet            Successfully pulled image "busybox" in 1.904s (2.621s including waiting)
  Normal   Pulled     70s                  kubelet            Successfully pulled image "busybox" in 1.811s (1.811s including waiting)
  Warning  BackOff    38s (x3 over 87s)    kubelet            Back-off restarting failed container post-install-container in pod post-install-hook_default(335333f8-5889-43a4-9314-3ea21e39536c)
  Normal   Pulling    22s (x4 over 2m14s)  kubelet            Pulling image "busybox"
  Normal   Created    21s (x4 over 2m10s)  kubelet            Created container post-install-container
  Normal   Pulled     21s                  kubelet            Successfully pulled image "busybox" in 1.872s (1.872s including waiting)
  Normal   Started    20s (x4 over 2m10s)  kubelet            Started container post-install-container
```

## I followed same steps for bonus task:
```shell
helm install app-js app-js/ --values app-js/values.yaml
```
### Output for `kubectl get pods,svc`
```shell
NAME                                       READY   STATUS      RESTARTS   AGE
pod/app-js-7489d5f8db-mrnwp                 1/1     Running     0          3m52s
pod/app-python-c5657fb4d-wkwz6              1/1     Running     0          5m11s
pod/post-install-hook                       0/1     Completed   0          3m52s
pod/pre-install-hook                        0/1     Completed   0          4m15s

NAME                          TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-js                LoadBalancer   10.103.33.251   <pending>     5001:32496/TCP   3m52s
service/app-python            LoadBalancer   10.102.33.229   <pending>     5000:31085/TCP   5m11s
service/kubernetes            ClusterIP      10.96.0.1       <none>        443/TCP          6m10s
```