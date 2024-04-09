# Lab 10: Helm
## Task 1

### Step 6 (`kubectl get pods,svc`)

```bash
NAME                            READY   STATUS    RESTARTS   AGE
pod/time-app-7f5f687c45-lvs6g   1/1     Running   0          8m23s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   30m
service/time-app     ClusterIP   10.105.95.229   <none>        80/TCP    8m23s
```

### Task 2

### Step 4

* #### `kubectl get po`
```bash
NAME                                   READY   STATUS      RESTARTS   AGE
helm-hooks-time-app-586fbdfcb7-gbnh9   1/1     Running     0          72s
postinstall-hook                       0/1     Completed   0          72s
preinstall-hook                        0/1     Completed   0          95s
time-app-7f5f687c45-lvs6g              1/1     Running     0          31m
```

* #### `kubectl describe po preinstall-hook`
```bash
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 17:53:11 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.11
IPs:
  IP:  10.244.0.11
Containers:
  pre-install-container:
    Container ID:  docker://9d05797c03cfa15df64935d37ad955371c04a8bfc6792803d9baa651cd6ed333
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
      Started:      Tue, 09 Apr 2024 17:53:12 +0300
      Finished:     Tue, 09 Apr 2024 17:53:32 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-ckq98 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-ckq98:
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
  Normal  Scheduled  111s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     110s  kubelet            Container image "busybox" already present on machine
  Normal  Created    110s  kubelet            Created container pre-install-container
  Normal  Started    110s  kubelet            Started container pre-install-container
```
* #### `kubectl describe po postinstall-hook`
```bash
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 17:53:34 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.13
IPs:
  IP:  10.244.0.13
Containers:
  post-install-container:
    Container ID:  docker://7f3f188ecf89fb3e3cb21a517dc2c7e6f57e3cebcaa4edf1ce8c1f8b267cb6c2
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
      Started:      Tue, 09 Apr 2024 17:53:38 +0300
      Finished:     Tue, 09 Apr 2024 17:53:53 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-gm9ds (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-gm9ds:
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
  Normal  Scheduled  99s   default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    98s   kubelet            Pulling image "busybox"
  Normal  Pulled     96s   kubelet            Successfully pulled image "busybox" in 2.607s (2.607s including waiting)
  Normal  Created    95s   kubelet            Created container post-install-container
  Normal  Started    95s   kubelet            Started container post-install-container
```

### After all steps

* #### `kubectl get pods,svc`
```bash
NAME                                       READY   STATUS    RESTARTS   AGE
pod/helm-hooks-time-app-586fbdfcb7-mldq8   1/1     Running   0          98s
pod/time-app-7f5f687c45-lvs6g              1/1     Running   0          35m

NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/helm-hooks-time-app   ClusterIP   10.96.51.249    <none>        80/TCP    98s
service/kubernetes            ClusterIP   10.96.0.1       <none>        443/TCP   57m
service/time-app              ClusterIP   10.105.95.229   <none>        80/TCP    35m
```