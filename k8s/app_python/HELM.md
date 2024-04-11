# Helm

## Task 1

```bash
DevOps on  lab10 [$✘!+?] took 3m 1.3s 
➜  kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-688b456bbd-nzl64   1/1     Running   0          3m19s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/app-python   ClusterIP   10.100.40.215   <none>        80/TCP    12m
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   13m
```

## Task 2

```bash
DevOps/k8s on  lab10 [⇡$!?] 
➜  kubectl get po
NAME                          READY   STATUS    RESTARTS   AGE
app-python-688b456bbd-nzl64   1/1     Running   0          19m
```

```bash
DevOps/k8s on  lab10 [⇡$!?] 
➜  kubectl get po                     
NAME                                  READY   STATUS      RESTARTS   AGE
helm-hooks-app-python-f8fc865-hpqbt   1/1     Running     0          71s
postinstall-hook                      0/1     Completed   0          71s
preinstall-hook                       0/1     Completed   0          84s
```

```bash
DevOps/k8s on  lab10 [⇡$!?] 
➜  kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.67.2
Start Time:       Fri, 12 Apr 2024 00:04:36 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.19
IPs:
  IP:  10.244.0.19
Containers:
  pre-install-container:
    Container ID:  docker://6362c6694cf0009cbe3a165e162a17005aafa7839e21d2e9b146b02fc07e045b
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 10
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Fri, 12 Apr 2024 00:04:37 +0300
      Finished:     Fri, 12 Apr 2024 00:04:47 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-ldtqd (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-ldtqd:
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
  Normal  Scheduled  3m7s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     3m6s  kubelet            Container image "busybox" already present on machine
  Normal  Created    3m6s  kubelet            Created container pre-install-container
  Normal  Started    3m6s  kubelet            Started container pre-install-container
```

```bash
DevOps/k8s on  lab10 [⇡$!?] 
➜  kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.67.2
Start Time:       Fri, 12 Apr 2024 00:04:49 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.21
IPs:
  IP:  10.244.0.21
Containers:
  pre-install-container:
    Container ID:  docker://0c3202fdcb36e04092da34319a1879958546423731fd36dfb8d2a71d71b12904
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 10
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Fri, 12 Apr 2024 00:04:50 +0300
      Finished:     Fri, 12 Apr 2024 00:05:00 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-jzdtl (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-jzdtl:
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
  Normal  Scheduled  3m52s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulled     3m51s  kubelet            Container image "busybox" already present on machine
  Normal  Created    3m51s  kubelet            Created container pre-install-container
  Normal  Started    3m51s  kubelet            Started container pre-install-container
```
