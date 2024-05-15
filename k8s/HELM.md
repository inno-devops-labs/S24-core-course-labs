# Helm

### 1st task

Verify the deployment:
`kubectl get pods,svc`

```
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-5b6bdb64f9-4m7qd   1/1     Running   0          3m19s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   NodePort    10.100.164.22   <none>        5000:30980/TCP   3m19s
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          9d
```

## Helm Chart Hooks

`kubectl get pods, svc`
```
NAME                          READY   STATUS      RESTARTS   AGE
app-python-5b6bdb64f9-9k2x6   1/1     Running     0          40s
postinstall-hook              0/1     Completed   0          40s
preinstall-hook               0/1     Completed   0          62s

NAME                            TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python              LoadBalancer   10.103.142.175   <pending>     5000:32072/TCP   62s
service/kubernetes              ClusterIP      10.96.0.1        <none>        443/TCP          6d19h
```

`kubectl get po`
```
NAME                                     READY   STATUS      RESTARTS   AGE
app-python-5b6bdb64f9-9k2x6              1/1     Running     0          20s
post-install-hook                        0/1     Completed   0          20s
pre-install-hook                         0/1     Completed   0          29s
``` 

`kubectl describe po post-install-hook`
``` 
Name:             post-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.105.2
Start Time:       Wed, 15 May 2024 14:02:01 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.57
IPs:
  IP:  10.244.0.57
Containers:
  sleep-10:
    Container ID:  docker://fcb19e7c7f3f204ecfd341c7b2a73f67a8cddaf5e9bed6c886cc29a1d78c0aa2
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sleep
    Args:
      10
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 15 May 2024 14:02:05 +0300
      Finished:     Wed, 15 May 2024 14:02:15 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-xkd6j (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-xkd6j:
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
  Normal  Scheduled  2m20s  default-scheduler  Successfully assigned default/post-install-hook to minikube
  Normal  Pulling    2m19s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m16s  kubelet            Successfully pulled image "busybox" in 1.521s (2.983s including waiting)
  Normal  Created    2m16s  kubelet            Created container sleep-10
  Normal  Started    2m16s  kubelet            Started container sleep-10
``` 

`kubectl describe po pre-install-hook`
``` 
Name:             pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.105.2
Start Time:       Wed, 15 May 2024 14:01:00 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.55
IPs:
  IP:  10.244.0.55
Containers:
  sleep-5:
    Container ID:  docker://5484913d4e58524f636666b5eb85967a9197621890e95527efbc314498b6c256
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sleep
    Args:
      5
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 15 May 2024 14:01:01 +0300
      Finished:     Wed, 15 May 2024 14:01:40 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-76kr5 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-76kr5:
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
  Normal  Scheduled  110s  default-scheduler  Successfully assigned default/pre-install-hook to minikube
  Normal  Pulling    109s  kubelet            Pulling image "busybox"
  Normal  Pulled     108s  kubelet            Successfully pulled image "busybox" in 1.541s (1.541s including waiting)
  Normal  Created    108s  kubelet            Created container sleep-5
  Normal  Started    108s  kubelet            Started container sleep-5
``` 