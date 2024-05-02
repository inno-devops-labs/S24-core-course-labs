# Helm

## Helm chart

```
$ kubectl get pods,svc
NAME                         READY   STATUS    RESTARTS   AGE
pod/app-py-774b8c9bc-4zqvs   1/1     Running   0          20s
pod/app-py-774b8c9bc-6tg64   1/1     Running   0          4m57s
pod/app-py-774b8c9bc-mhm8j   1/1     Running   0          4m57s
pod/app-py-774b8c9bc-zsb2b   1/1     Running   0          4m57s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-py       LoadBalancer   10.106.188.219   <pending>     5000:30928/TCP   4m57s
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          21m
$
```

## Helm hooks

```
$ kubectl get po
NAME                     READY   STATUS      RESTARTS   AGE
app-py-774b8c9bc-2rfbf   1/1     Running     0          86s
app-py-774b8c9bc-6dz7d   1/1     Running     0          86s
app-py-774b8c9bc-bzpqf   1/1     Running     0          86s
app-py-774b8c9bc-z9l76   1/1     Running     0          86s
post-install-hook        0/1     Completed   0          86s
pre-install-hook         0/1     Completed   0          100s
$ kubectl describe po pre-install-hook
Name:             pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 31 Mar 2024 22:15:29 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.25
IPs:
  IP:  10.244.0.25
Containers:
  sleep-5:
    Container ID:  docker://dd1fcb8f5e49cb0a4b655c1b50f86980b777448f40b9efb10b188e62b4faf181
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
      Started:      Sun, 31 Mar 2024 22:15:35 +0300
      Finished:     Sun, 31 Mar 2024 22:15:40 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-52w28 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-52w28:
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
  Normal  Scheduled  106s  default-scheduler  Successfully assigned default/pre-install-hook to minikube
  Normal  Pulling    103s  kubelet            Pulling image "busybox"
  Normal  Pulled     101s  kubelet            Successfully pulled image "busybox" in 2.166s (2.167s including waiting)
  Normal  Created    100s  kubelet            Created container sleep-5
  Normal  Started    100s  kubelet            Started container sleep-5
$ kubectl describe po post-install-hook
Name:             post-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 31 Mar 2024 22:15:43 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.29
IPs:
  IP:  10.244.0.29
Containers:
  sleep-10:
    Container ID:  docker://90f8d485d239cb251abb96bed98bb057023e0026bd0f44a519f4020c04e10b8e
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
      Started:      Sun, 31 Mar 2024 22:15:49 +0300
      Finished:     Sun, 31 Mar 2024 22:15:59 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-nlrcb (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-nlrcb:
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
  Normal  Scheduled  99s   default-scheduler  Successfully assigned default/post-install-hook to minikube
  Normal  Pulling    97s   kubelet            Pulling image "busybox"
  Normal  Pulled     95s   kubelet            Successfully pulled image "busybox" in 2.015s (2.015s including waiting)
  Normal  Created    95s   kubelet            Created container sleep-10
  Normal  Started    94s   kubelet            Started container sleep-10
$ kubectl get pods,svc
NAME                         READY   STATUS    RESTARTS   AGE
pod/app-py-774b8c9bc-hv6tg   1/1     Running   0          67s
pod/app-py-774b8c9bc-p2v9s   1/1     Running   0          67s
pod/app-py-774b8c9bc-r22dh   1/1     Running   0          67s
pod/app-py-774b8c9bc-svlbm   1/1     Running   0          67s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-py       LoadBalancer   10.111.233.19   <pending>     5000:31628/TCP   67s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          113m
$
```
