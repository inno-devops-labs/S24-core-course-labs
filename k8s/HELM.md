# Helm

## Outputs

### 1.

- `kubectl get pods,svc`


```bash
NAME                                                 READY   STATUS    RESTARTS      AGE
pod/moscow-time-app-deployment-68d6d9b7d8-54ct2      1/1     Running   1 (27m ago)   5d23h
pod/moscow-time-app-deployment-68d6d9b7d8-cz4jd      1/1     Running   1 (27m ago)   5d23h
pod/moscow-time-app-deployment-68d6d9b7d8-gl6n8      1/1     Running   1 (27m ago)   5d23h
pod/moscow-time-app-js-deployment-7c5f8ccc47-6lj4q   1/1     Running   1 (27m ago)   5d23h
pod/moscow-time-app-js-deployment-7c5f8ccc47-mwzlx   1/1     Running   1 (27m ago)   5d23h
pod/moscow-time-app-js-deployment-7c5f8ccc47-xmg4j   1/1     Running   1 (27m ago)   5d23h
pod/pythonrelease-helm-app-python-7d8f87847d-4q6j7   1/1     Running   0             6m45s

NAME                                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes                      ClusterIP   10.96.0.1       <none>        443/TCP          6d5h
service/moscow-time-app-js-service      NodePort    10.98.106.67    <none>        3000:30945/TCP   5d23h
service/moscow-time-app-service         NodePort    10.97.223.176   <none>        8000:31274/TCP   5d23h
service/pythonrelease-helm-app-python   ClusterIP   10.103.253.68   <none>        8000/TCP         6m45s
```

### 2.

 - `kubectl get po` 

 ```bash
 NAME                                             READY   STATUS      RESTARTS      AGE
app-python-statefulset-0                         1/1     Running     0             4m43s
moscow-time-app-deployment-68d6d9b7d8-54ct2      1/1     Running     1 (60m ago)   6d
moscow-time-app-deployment-68d6d9b7d8-cz4jd      1/1     Running     1 (60m ago)   6d
moscow-time-app-deployment-68d6d9b7d8-gl6n8      1/1     Running     1 (60m ago)   6d
moscow-time-app-js-deployment-7c5f8ccc47-6lj4q   1/1     Running     1 (60m ago)   5d23h
moscow-time-app-js-deployment-7c5f8ccc47-mwzlx   1/1     Running     1 (60m ago)   5d23h
moscow-time-app-js-deployment-7c5f8ccc47-xmg4j   1/1     Running     1 (60m ago)   5d23h
postinstall-hook                                 0/1     Completed   0             4m43s
preinstall-hook                                  0/1     Completed   0             5m15s
```

 - `kubectl describe po preinstall-hook`

```bash
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Mon, 08 Apr 2024 21:06:32 +0000
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.39
IPs:
  IP:  10.244.0.39
Containers:
  pre-install-container:
    Container ID:  docker://ee5ebc698842027e4e41d5c15f837919758d54b748e769f497b280634e0e4130
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
      Started:      Mon, 08 Apr 2024 21:06:41 +0000
      Finished:     Mon, 08 Apr 2024 21:07:01 +0000
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-k5s2s (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-k5s2s:
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
  Normal  Scheduled  6m6s   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    6m6s   kubelet            Pulling image "busybox"
  Normal  Pulled     5m58s  kubelet            Successfully pulled image "busybox" in 8.02s (8.02s including waiting)
  Normal  Created    5m58s  kubelet            Created container pre-install-container
  Normal  Started    5m58s  kubelet            Started container pre-install-container
```


 - `kubectl describe po postinstall-hook`

```bash
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Mon, 08 Apr 2024 21:07:04 +0000
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.41
IPs:
  IP:  10.244.0.41
Containers:
  post-install-container:
    Container ID:  docker://1016c97533be550fd7ff176208a6e7240330349cba2d0ba7b9773020173bb7b9
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
      Started:      Mon, 08 Apr 2024 21:07:10 +0000
      Finished:     Mon, 08 Apr 2024 21:07:25 +0000
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-sdmjv (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-sdmjv:
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
  Normal  Scheduled  6m14s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    6m13s  kubelet            Pulling image "busybox"
  Normal  Pulled     6m8s   kubelet            Successfully pulled image "busybox" in 2.657s (5.317s including waiting)
  Normal  Created    6m8s   kubelet            Created container post-install-container
  Normal  Started    6m8s   kubelet            Started container post-install-container
```
