# HELM

## Task 1

### Output of `kubectl get pods,svc`

```text
NAME                                         READY   STATUS    RESTARTS        AGE
pod/app-app-python-7f8b498466-bq96w          1/1     Running   0               2m16s

NAME                            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/app-app-python          ClusterIP   10.100.85.197   <none>        8000/TCP   2m21s
service/kubernetes              ClusterIP   10.96.0.1       <none>        443/TCP    5d23h
```

## Task 2

### Output of `kubectl get po`

```text
NAME                                     READY   STATUS      RESTARTS   AGE
app-app-python-7f8b498466-6cg5g          1/1     Running     0          19m
helm-hooks-app-python-58947cb96b-8t5xp   1/1     Running     0          6m59s
post-install-hook                        0/1     Completed   0          6m58s
pre-install-hook                         0/1     Completed   0          7m21s
```

### Output of `kubectl describe po pre-install-hook`

```text
Name:             pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 10:37:51 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
                  helm.sh/hook-delete-policy: before-hook-creation
Status:           Succeeded
IP:               10.244.0.9
IPs:
  IP:  10.244.0.9
Containers:
  pre-install-container:
    Container ID:  docker://efc692287ef92399afe9da4b959574fd87af71b177f24ef76651e5ed002ff792
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
      Started:      Wed, 10 Apr 2024 10:37:51 +0300
      Finished:     Wed, 10 Apr 2024 10:38:11 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-z225p (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-z225p:
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
  Normal  Scheduled  47s   default-scheduler  Successfully assigned default/pre-install-hook to minikube
  Normal  Pulled     47s   kubelet            Container image "busybox" already present on machine
  Normal  Created    47s   kubelet            Created container pre-install-container
  Normal  Started    47s   kubelet            Started container pre-install-container
```

### Output of `kubectl describe po post-install-hook`

```text
Name:             post-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 10:38:14 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
                  helm.sh/hook-delete-policy: before-hook-creation
Status:           Succeeded
IP:               10.244.0.10
IPs:
  IP:  10.244.0.10
Containers:
  post-install-container:
    Container ID:  docker://dddab0068be2654da06eb4bfb25a383006c5068ba0daf2effc95957b1e828ce7
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
      Started:      Wed, 10 Apr 2024 10:38:17 +0300
      Finished:     Wed, 10 Apr 2024 10:38:32 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-lbghp (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-lbghp:
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
  Normal  Scheduled  35s   default-scheduler  Successfully assigned default/post-install-hook to minikube
  Normal  Pulling    35s   kubelet            Pulling image "busybox"
  Normal  Pulled     32s   kubelet            Successfully pulled image "busybox" in 2.567s (2.567s including waiting)
  Normal  Created    32s   kubelet            Created container post-install-container
  Normal  Started    32s   kubelet            Started container post-install-container
```
