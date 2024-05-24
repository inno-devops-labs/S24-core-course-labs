# HELM

## kubectl get pods,svc

```
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-7d97876598-n4zkv   1/1     Running   0          64s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   NodePort    10.108.29.230   <none>        8000:32566/TCP   64s
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          8h
```

## kubectl get po

```
NAME               READY   STATUS      RESTARTS   AGE
postinstall-hook   0/1     Completed   0          99s
preinstall-hook    0/1     Completed   0          2m8s
```

## kubectl describe po preinstall-hook

```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Fri, 24 May 2024 14:20:30 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.23
IPs:
  IP:  10.244.0.23
Containers:
  pre-install-container:
    Container ID:  docker://f90a4b3dd31de14e27f884e4c7e9b95f4838cc10c9c68728bf8114b08463e671
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:5eef5ed34e1e1ff0a4ae850395cbf665c4de6b4b83a32a0bc7bcb998e24e7bbb
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Fri, 24 May 2024 14:20:37 +0300
      Finished:     Fri, 24 May 2024 14:20:57 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-wzs4z (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-wzs4z:
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
  Normal  Scheduled  2m44s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    2m44s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m38s  kubelet            Successfully pulled image "busybox" in 6.276s (6.276s including waiting)
  Normal  Created    2m38s  kubelet            Created container pre-install-container
  Normal  Started    2m38s  kubelet            Started container pre-install-container
```

## kubectl describe po postinstall-hook

```
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Fri, 24 May 2024 14:20:59 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.24
IPs:
  IP:  10.244.0.24
Containers:
  post-install-container:
    Container ID:  docker://b47e1288319e4a8a81d931b8f73578cbc54c11bb93f321fbca9dfd8af8ee80ba
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:5eef5ed34e1e1ff0a4ae850395cbf665c4de6b4b83a32a0bc7bcb998e24e7bbb
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 15
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Fri, 24 May 2024 14:21:02 +0300
      Finished:     Fri, 24 May 2024 14:21:17 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-jz5ct (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-jz5ct:
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
  Normal  Scheduled  2m45s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    2m46s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m43s  kubelet            Successfully pulled image "busybox" in 2.929s (2.929s including waiting)
  Normal  Created    2m43s  kubelet            Created container post-install-container
  Normal  Started    2m43s  kubelet            Started container post-install-container
```

