# Helm

## Task 1

```
$ kubectl get pods,svc
NAME                                         READY   STATUS    RESTARTS   AGE
pod/app-python-1712487052-5fbf66874d-qkxtv   1/1     Running   0          2m43s

NAME                            TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/app-python-1712487052   ClusterIP   10.111.132.210   <none>        8080/TCP   2m43s
service/kubernetes              ClusterIP   10.96.0.1        <none>        443/TCP    9m33s
```

## Task 2

```
$ kubectl get po
NAME                                     READY   STATUS      RESTARTS   AGE
app-python-1712487052-5fbf66874d-qkxtv   1/1     Running     0          40m
helm-hooks-app-python-f8cf4f847-bcnm9    1/1     Running     0          46s
postinstall-hook                         0/1     Completed   0          46s
preinstall-hook                          0/1     Completed   0          77s
```

```
$ kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 07 Apr 2024 14:30:34 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.9
IPs:
  IP:  10.244.0.9
Containers:
  pre-install-container:
    Container ID:  containerd://6835ac894297bbdfdec7594f3944e18fb5e4a5539c228b785462be650a2cde4b
    Image:         busybox
    Image ID:      docker.io/library/busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 07 Apr 2024 14:30:42 +0300
      Finished:     Sun, 07 Apr 2024 14:31:02 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-strtd (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-strtd:
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
  Normal  Scheduled  99s   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    96s   kubelet            Pulling image "busybox"
  Normal  Pulled     91s   kubelet            Successfully pulled image "busybox" in 5.324s (5.336s including waiting)
  Normal  Created    91s   kubelet            Created container pre-install-container
  Normal  Started    91s   kubelet            Started container pre-install-container
```

```
$ kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 07 Apr 2024 14:31:06 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.11
IPs:
  IP:  10.244.0.11
Containers:
  post-install-container:
    Container ID:  containerd://b1ad5d17f67c176c6bac31f71d2276e44e40578a5c43b4e5d8632755d4e7ddf2
    Image:         busybox
    Image ID:      docker.io/library/busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 15
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 07 Apr 2024 14:31:08 +0300
      Finished:     Sun, 07 Apr 2024 14:31:23 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-rtmpd (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-rtmpd:
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
  Normal  Scheduled  90s   default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    90s   kubelet            Pulling image "busybox"
  Normal  Pulled     88s   kubelet            Successfully pulled image "busybox" in 1.342s (1.342s including waiting)
  Normal  Created    88s   kubelet            Created container post-install-container
  Normal  Started    88s   kubelet            Started container post-install-container
```
