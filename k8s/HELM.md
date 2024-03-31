# Lab 10: Introduction to Helm

## Task 1: Helm Setup and Chart Creation

### Output of `kubectl get pods,svc`

```text
NAME                                             READY   STATUS    RESTARTS   AGE
pod/mv-app-python-app-py-helm-7d5fb445b4-vmxmd   1/1     Running   0          3m1s

NAME                                TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
service/kubernetes                  ClusterIP      10.96.0.1     <none>        443/TCP          3d9h
service/mv-app-python-app-py-helm   LoadBalancer   10.107.3.47   <pending>     5000:32401/TCP   3m1s
```

## Task 2: Helm Chart Hooks

### Output of commands

```text
~/D/S/k8s (lab10)> kubectl get po
NAME                                         READY   STATUS      RESTARTS   AGE
mv-app-python-app-py-helm-7d5fb445b4-2bkw5   1/1     Running     0          21s
postinstall-hook                             0/1     Completed   0          21s
preinstall-hook                              0/1     Completed   0          31s
~/D/S/k8s (lab10)> kubectl describe po preinstall-hook 
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Mon, 01 Apr 2024 01:32:51 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.35
IPs:
  IP:  10.244.0.35
Containers:
  sleep-3:
    Container ID:  docker://749751a7d9d083019f5efcec02c752f0a91b9e79c98324d6d9fbf0a4bb72f53e
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 3
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Mon, 01 Apr 2024 01:32:56 +0300
      Finished:     Mon, 01 Apr 2024 01:32:59 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-fj49h (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-fj49h:
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
  Normal  Scheduled  46s   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    47s   kubelet            Pulling image "busybox"
  Normal  Pulled     42s   kubelet            Successfully pulled image "busybox" in 5.188s (5.188s including waiting)
  Normal  Created    42s   kubelet            Created container sleep-3
  Normal  Started    42s   kubelet            Started container sleep-3
~/D/S/k8s (lab10)> kubectl describe po postinstall-hook 
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Mon, 01 Apr 2024 01:33:01 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.37
IPs:
  IP:  10.244.0.37
Containers:
  sleep-3:
    Container ID:  docker://21dce0f58506369d7aab6a3d94b6bf8ee6f8325487f9954b55f5676af31bc44f
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 3
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Mon, 01 Apr 2024 01:33:02 +0300
      Finished:     Mon, 01 Apr 2024 01:33:05 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-vfzt5 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-vfzt5:
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
  Normal  Scheduled  43s   default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulled     43s   kubelet            Container image "busybox" already present on machine
  Normal  Created    43s   kubelet            Created container sleep-3
  Normal  Started    43s   kubelet            Started container sleep-3
```

### Output of `kubectl get pods, svc`

```text
NAME                                             READY   STATUS    RESTARTS   AGE
pod/mv-app-python-app-py-helm-7d5fb445b4-xhwkl   1/1     Running   0          40s

NAME                                TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes                  ClusterIP      10.96.0.1       <none>        443/TCP          3d10h
service/mv-app-python-app-py-helm   LoadBalancer   10.103.17.184   <pending>     5000:31043/TCP   40s
```
