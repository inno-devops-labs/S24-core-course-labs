# HELM

### Task 1: Helm Setup and Chart Creation

Output of `kubectl get pods,svc`:

```
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-8ac72o22h-jra39   1/1     Running   0          11s

NAME                        TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python          ClusterIP      10.110.128.71   <none>        5000/TCP         11s
service/kubernetes          ClusterIP      10.96.0.1       <none>        443/TCP          59s
```


### Task 2: Helm Chart Hooks

Output of `kubectl get po`:

```
NAME                                     READY   STATUS      RESTARTS   AGE
app-python-8ac72o22h-jra39               1/1     Running     0          31s
helm-hooks-app-python-87a03gbhr-kj208    1/1     Running     0          34s
postinstall-hook                         0/1     Completed   0          34s
preinstall-hook                          0/1     Completed   0          57s
```


Output of `kubectl describe po preinstall_hook`:

```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 14:14:21 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.9
IPs:
  IP:  10.244.0.9
Containers:
  pre-install-container:
    Container ID:  docker://4b2926e58a974b26629254a4b7e1352a9757d44e837426d9041dd92426e7139e
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
      Started:      Tue, 09 Apr 2024 14:14:22 +0300
      Finished:     Tue, 09 Apr 2024 14:14:42 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-j1sm2 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-j1sm2:
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
  Normal  Scheduled  65s   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     65s   kubelet            Container image "busybox" already present on machine
  Normal  Created    65s   kubelet            Created container pre-install-container
  Normal  Started    65s   kubelet            Started container pre-install-container
```


Output of `kubectl describe po postinstall_hook`:

```
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 14:14:44 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.11
IPs:
  IP:  10.244.0.11
Containers:
  post-install-container:
    Container ID:  docker://7d8791a26e484d79187947e7d1b203e6484fc78a927618b0532aa8434de2706b
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
      Started:      Tue, 09 Apr 2024 14:14:46 +0300
      Finished:     Tue, 09 Apr 2024 14:15:01 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-a5l0f (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-a5l0f:
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
  Normal  Scheduled  121s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    120s  kubelet            Pulling image "busybox"
  Normal  Pulled     118s  kubelet            Successfully pulled image "busybox" in 1.988s (1.988s including waiting)
  Normal  Created    118s  kubelet            Created container post-install-container
  Normal  Started    118s  kubelet            Started container post-install-container
```
