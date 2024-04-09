# Task 1
`kubectl get pods,svc`
```sh
PS D:\MINE\Repositories\DevOps\k8s> kubectl get pods,svc
NAME                             READY   STATUS      RESTARTS   AGE
pod/app-python-75b86989c-x4lc2   1/1     Running     0          38s

NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/app-python   ClusterIP   10.104.1.222   <none>        5000/TCP   38s
service/kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP    74m
```

# Task 2 
`kubectl get po`
```sh
PS D:\MINE\Repositories\DevOps\k8s> kubectl get po
NAME                         READY   STATUS      RESTARTS   AGE
app-python-75b86989c-x4lc2   1/1     Running     0          2m25s
postinstall-hook             0/1     Completed   0          4m28s
preinstall-hook              0/1     Completed   0          4m50s
```

`kubectl describe po preinstall-hook` Sleeps for 20 seconds
```sh
PS D:\MINE\Repositories\DevOps\k8s> kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 22:51:41 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.9
IPs:
  IP:  10.244.0.9
Containers:
  pre-install-container:
    Container ID:  docker://9e0708e9b01b637dfc3a0cd78c44d83b4804021b23214549534d81f3e3e9527e
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
      Started:      Tue, 09 Apr 2024 22:51:41 +0300
      Finished:     Tue, 09 Apr 2024 22:52:01 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-wrt5c (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-wrt5c:
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
  Normal  Scheduled  8m25s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     8m25s  kubelet            Container image "busybox" already present on machine
  Normal  Created    8m25s  kubelet            Created container pre-install-container
  Normal  Started    8m25s  kubelet            Started container pre-install-container
```

`kubectl describe po postinstall-hook` Sleeps for 15 seconds
```sh
PS D:\MINE\Repositories\DevOps\k8s> kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 22:52:03 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.11
IPs:
  IP:  10.244.0.11
Containers:
  post-install-container:
    Container ID:  docker://86d6cee0c6751d008e497e31940f13d4a132b4ad2621c8613552e209e73f0f1d
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
      Started:      Tue, 09 Apr 2024 22:52:06 +0300
      Finished:     Tue, 09 Apr 2024 22:52:21 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-4hwxm (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-4hwxm:
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
  Normal  Scheduled  9m7s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    9m6s  kubelet            Pulling image "busybox"
  Normal  Pulled     9m4s  kubelet            Successfully pulled image "busybox" in 1.912s (1.912s including waiting)
  Normal  Created    9m4s  kubelet            Created container post-install-container
  Normal  Started    9m4s  kubelet            Started container post-install-container
```