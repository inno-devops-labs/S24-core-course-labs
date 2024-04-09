# Task 1

```
❯ kubectl get pods,svc
NAME                                           READY   STATUS      RESTARTS   AGE
pod/helm-hooks-manual-flask-5f655c6f7f-bnjp5   1/1     Running     0          3m27s
pod/manual-flask-1712682621-677c885b99-n8mkw   1/1     Running     0          26m
pod/mysql-1712682020-0                         1/1     Running     0          36m
pod/postinstall-hook                           0/1     Completed   0          3m27s
pod/preinstall-hook                            0/1     Completed   0          3m50s

NAME                              TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/helm-hooks-manual-flask   LoadBalancer   10.98.5.42     <pending>     5000:32726/TCP   3m27s
service/kubernetes                ClusterIP      10.96.0.1      <none>        443/TCP          46m
service/manual-flask-1712682621   LoadBalancer   10.99.116.33   <pending>     5000:31862/TCP   26m

# Task 2

```text
❯ kubectl get po

NAME                                       READY   STATUS      RESTARTS   AGE
helm-hooks-manual-flask-5f655c6f7f-bnjp5   1/1     Running     0          26s
manual-flask-1712682621-677c885b99-n8mkw   1/1     Running     0          23m
mysql-1712682020-0                         1/1     Running     0          33m
postinstall-hook                           0/1     Completed   0          26s
preinstall-hook                            0/1     Completed   0          49s
```

```
❯ kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 20:33:39 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.18
IPs:
  IP:  10.244.0.18
Containers:
  post-install-container:
    Container ID:  docker://18deacf1d170cef7c694e4b73e0fcd3971b4c8147bf846b1c2cc7d5d4fb3508e
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
      Started:      Tue, 09 Apr 2024 20:33:42 +0300
      Finished:     Tue, 09 Apr 2024 20:33:57 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-h89gv (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-h89gv:
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
  Normal  Scheduled  2m8s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    2m7s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m6s  kubelet            Successfully pulled image "busybox" in 1.849s (1.849s including waiting)
  Normal  Created    2m6s  kubelet            Created container post-install-container
  Normal  Started    2m5s  kubelet            Started container post-install-container
```


```
❯ kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 20:33:16 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.17
IPs:
  IP:  10.244.0.17
Containers:
  pre-install-container:
    Container ID:  docker://89a67a2f343f119095e7b8886b79011cfba5cb9f782562f685b26bebf394b4ab
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
      Started:      Tue, 09 Apr 2024 20:33:17 +0300
      Finished:     Tue, 09 Apr 2024 20:33:37 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-cqrhc (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-cqrhc:
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
  Normal  Scheduled  3m1s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     3m    kubelet            Container image "busybox" already present on machine
  Normal  Created    3m    kubelet            Created container pre-install-container
  Normal  Started    3m    kubelet            Started container pre-install-container
```