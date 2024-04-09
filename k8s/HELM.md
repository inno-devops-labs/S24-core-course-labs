## Output of `kubectl get pods,svc`

```
NAME                                                 READY   STATUS    RESTARTS   AGE
pod/app-python-release-python-app-65777fbfbd-dbzrn   1/1     Running   0          43s

NAME                                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/app-python-release-python-app   NodePort    10.96.137.164   <none>        80:32427/TCP   80m
service/kubernetes                      ClusterIP   10.96.0.1       <none>        443/TCP        6d21h
```

## Output of `kubectl get po`
```
NAME                                             READY   STATUS      RESTARTS       AGE
app-python-release-python-app-65777fbfbd-dbzrn   1/1     Running     1 (6h7m ago)   28h
helm-hooks-python-app-5bcccc7b55-fmvjd           1/1     Running     0              2m17s
postinstall-hook                                 0/1     Completed   0              2m17s
preinstall-hook                                  0/1     Completed   0              3m2s
```

## Output of `kubectl describe po preinstall-hook`
```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 17:31:18 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.25
IPs:
  IP:  10.244.0.25
Containers:
  pre-install-container:
    Container ID:  docker://386396bfd3166265ce7389eda4b37040ffa9afca9ac40ec7c61a67a223e0e3ce
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
      Started:      Tue, 09 Apr 2024 17:31:42 +0300
      Finished:     Tue, 09 Apr 2024 17:32:02 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-s6qp7 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-s6qp7:
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
  Normal  Scheduled  4m18s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    4m18s  kubelet            Pulling image "busybox"
  Normal  Pulled     3m54s  kubelet            Successfully pulled image "busybox" in 23.313s (23.313s including waiting)
  Normal  Created    3m54s  kubelet            Created container pre-install-container
  Normal  Started    3m54s  kubelet            Started container pre-install-container
```

## Output of `kubectl describe po postinstall-hook`
```
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 17:32:03 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.27
IPs:
  IP:  10.244.0.27
Containers:
  post-install-container:
    Container ID:  docker://68c9ca1f5d01579a29e5a2d8d23a44f5fd8a517c4cdb38bc97f84379d2d1ba0f
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
      Started:      Tue, 09 Apr 2024 17:32:09 +0300
      Finished:     Tue, 09 Apr 2024 17:32:24 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-mj89f (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-mj89f:
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
  Normal  Scheduled  3m59s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    3m59s  kubelet            Pulling image "busybox"
  Normal  Pulled     3m54s  kubelet            Successfully pulled image "busybox" in 4.598s (4.598s including waiting)
  Normal  Created    3m54s  kubelet            Created container post-install-container
  Normal  Started    3m54s  kubelet            Started container post-install-container
```