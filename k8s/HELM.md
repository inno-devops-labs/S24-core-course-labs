# Output of `kubectl get pods,svc`

```
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-8478df6699-2bhsh   1/1     Running   0          2m11s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/app-python   ClusterIP   10.101.203.239   <none>        8000/TCP   2m11s
service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP    8d
```

# Output of `kubectl get po`

```
NAME                                    READY   STATUS      RESTARTS   AGE
helm-hooks-app-python-8477c884b-9mwmm   1/1     Running     0          102m
postinstall-hook                        0/1     Completed   0          102m
preinstall-hook                         0/1     Completed   0          102m
```

# Output of `kubectl describe po preinstall-hook`

```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 20:40:24 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.44
IPs:
  IP:  10.244.0.44
Containers:
  pre-install-container:
    Container ID:  docker://652ee26fa659501ac8241b13bb159536ddacacfb89d7b895e59f9efa92c31a31
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
      Started:      Tue, 09 Apr 2024 20:40:25 +0300
      Finished:     Tue, 09 Apr 2024 20:40:45 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-w9cvq (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-w9cvq:
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
  Normal  Scheduled  103m  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     103m  kubelet            Container image "busybox" already present on machine
  Normal  Created    103m  kubelet            Created container pre-install-container
  Normal  Started    103m  kubelet            Started container pre-install-container
```

# Output of `kubectl describe po postinstall-hook`

```
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 20:40:47 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.45
IPs:
  IP:  10.244.0.45
Containers:
  post-install-container:
    Container ID:  docker://2ab2c3a40b0c113cc561794b01015abac87d1873392f90c38ca843958aa907d3
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
      Started:      Tue, 09 Apr 2024 20:40:50 +0300
      Finished:     Tue, 09 Apr 2024 20:41:05 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-5hpr9 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-5hpr9:
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
  Normal  Scheduled  104m  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    104m  kubelet            Pulling image "busybox"
  Normal  Pulled     104m  kubelet            Successfully pulled image "busybox" in 2.446s (2.446s including waiting)
  Normal  Created    104m  kubelet            Created container post-install-container
  Normal  Started    104m  kubelet            Started container post-install-container
```
