# HELM

# Task 1

```sh
❯ kubectl get pods,svc
NAME                                        READY   STATUS    RESTARTS   AGE
pod/helm-chart-app-python-99f498477-mnrfz   1/1     Running   0          76s

NAME                            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/helm-chart-app-python   ClusterIP   10.109.33.199   <none>        80/TCP    76s
service/kubernetes              ClusterIP   10.96.0.1       <none>        443/TCP   16m
```

# Task 2

```sh
❯ kubectl get po
NAME                                    READY   STATUS      RESTARTS   AGE
helm-chart-app-python-99f498477-mnrfz   1/1     Running     0          11m
postinstall-hook                        0/1     Completed   0          43s
preinstall-hook                         0/1     Completed   0          49s
```

```sh
❯ kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Mon, 08 Apr 2024 19:36:38 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.9
IPs:
  IP:  10.244.0.9
Containers:
  pre-install-container:
    Container ID:  docker://2b2ddf14a3b1aafab4f3b6e079408894a4deb9553f76b8afe158e9ba1589e87b
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
      Started:      Mon, 08 Apr 2024 19:36:38 +0300
      Finished:     Mon, 08 Apr 2024 19:36:41 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-kbd7v (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-kbd7v:
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
  Normal  Scheduled  2m18s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     2m18s  kubelet            Container image "busybox" already present on machine
  Normal  Created    2m18s  kubelet            Created container pre-install-container
  Normal  Started    2m18s  kubelet            Started container pre-install-container
```

```sh
❯ kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Mon, 08 Apr 2024 19:36:44 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.10
IPs:
  IP:  10.244.0.10
Containers:
  post-install-container:
    Container ID:  docker://2fe31308f2572249be55ca66459d46ae67f158063e76a1beb06518f717d19d4c
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
      Started:      Mon, 08 Apr 2024 19:36:46 +0300
      Finished:     Mon, 08 Apr 2024 19:36:49 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-xhhz4 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-xhhz4:
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
  Normal  Scheduled  2m20s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    2m20s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m18s  kubelet            Successfully pulled image "busybox" in 1.849s (1.849s including waiting)
  Normal  Created    2m18s  kubelet            Created container post-install-container
  Normal  Started    2m18s  kubelet            Started container post-install-container
```
