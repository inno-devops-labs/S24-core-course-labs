# Helm

## kubectl get po

```bash
$ kubectl get po
NAME                                  READY   STATUS      RESTARTS   AGE
app-python-74c48c6b74-55cnm           1/1     Running     0          3h37m
app-python-74c48c6b74-6cv8q           1/1     Running     0          3h37m
app-python-74c48c6b74-lppxm           1/1     Running     0          3h48m
helm-hooks-web-app-748468895b-84zhz   1/1     Running     0          53s
postinstall-hook                      0/1     Completed   0          53s
preinstall-hook                       0/1     Completed   0          76s
```

## kubectl describe po preinstall-hook

```bash
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Mon, 02 Sep 2024 21:53:25 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.15
IPs:
  IP:  10.244.0.15
Containers:
  pre-install-container:
    Container ID:  docker://7db24bb0f3df0433e1203b4088f533460da8291eaf95b26dd79ff55c42934c3a
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:82742949a3709938cbeb9cec79f5eaf3e48b255389f2dcedf2de29ef96fd841c
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Mon, 02 Sep 2024 21:53:30 +0300
      Finished:     Mon, 02 Sep 2024 21:53:50 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-vgcbj (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-vgcbj:
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
  Normal  Scheduled  4m30s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    4m29s  kubelet            Pulling image "busybox"
  Normal  Pulled     4m25s  kubelet            Successfully pulled image "busybox" in 3.921s (3.921s including waiting). Image size: 4261574 bytes.
  Normal  Created    4m25s  kubelet            Created container pre-install-container
  Normal  Started    4m25s  kubelet            Started container pre-install-container
```

## kubectl describe po postinstall-hook

```bash
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Mon, 02 Sep 2024 21:53:53 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.17
IPs:
  IP:  10.244.0.17
Containers:
  post-install-container:
    Container ID:  docker://b2cbc171c44e58e67aa24246a609e6fd920eaaa857cd4528fb028c3b2d23d4fa
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:82742949a3709938cbeb9cec79f5eaf3e48b255389f2dcedf2de29ef96fd841c
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo post-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Mon, 02 Sep 2024 21:53:55 +0300
      Finished:     Mon, 02 Sep 2024 21:54:15 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-t6qtj (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-t6qtj:
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
  Normal  Scheduled  5m12s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    5m12s  kubelet            Pulling image "busybox"
  Normal  Pulled     5m10s  kubelet            Successfully pulled image "busybox" in 1.42s (1.42s including waiting). Image size: 4261574 bytes.
  Normal  Created    5m10s  kubelet            Created container post-install-container
  Normal  Started    5m10s  kubelet            Started container post-install-container
```
