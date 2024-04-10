# Helm

## Setup status

```bash
$  kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE          
pod/app-python-7f86db6bb9-49qld   1/1     Running   0          4m8s         
                                                                            
NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/app-python   ClusterIP   10.103.209.31   <none>        80/TCP    4m8s
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   38h
```

## Setup status with hooks

```bash
$ kubectl get po                       
NAME                          READY   STATUS      RESTARTS   AGE
app-python-7f86db6bb9-6wlkx   1/1     Running     0          37s
postinstall-hook              0/1     Completed   0          37s
preinstall-hook               0/1     Completed   0          67s
```

```bash
$ kubectl describe po preinstall-hook            
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 09:11:53 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.12
IPs:
  IP:  10.244.0.12
Containers:
  pre-install-container:
    Container ID:  docker://da2e911c3f9686358b83f759827bad3976b453cdc0e5f077578b4d6b5419f045
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The app-python pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 10 Apr 2024 09:12:01 +0300
      Finished:     Wed, 10 Apr 2024 09:12:21 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-qrcvq (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-qrcvq:
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
  Normal  Scheduled  89s   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    89s   kubelet            Pulling image "busybox"
  Normal  Pulled     81s   kubelet            Successfully pulled image "busybox" in 7.997s (7.997s including waiting)
  Normal  Created    81s   kubelet            Created container pre-install-container
  Normal  Started    81s   kubelet            Started container pre-install-container
```

```bash
$ kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 09:12:23 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.14
IPs:
  IP:  10.244.0.14
Containers:
  post-install-container:
    Container ID:  docker://601fd815f7f20c434e3c43b206a13263c16ab05254ce273238554f7539cd5c01
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The app-python post-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 10 Apr 2024 09:12:26 +0300
      Finished:     Wed, 10 Apr 2024 09:12:46 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-j2f4p (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-j2f4p:
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
  Normal  Scheduled  92s   default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    92s   kubelet            Pulling image "busybox"
  Normal  Pulled     90s   kubelet            Successfully pulled image "busybox" in 2.059s (2.059s including waiting)
  Normal  Created    90s   kubelet            Created container post-install-container
  Normal  Started    90s   kubelet            Started container post-install-container
```
