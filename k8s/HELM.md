# Introduction to HELM

## Task 1

- After running `helm install time-app time-app`:
```
$ kubectl get pods,svc
NAME                            READY   STATUS    RESTARTS   AGE
pod/time-app-68c949f656-xbjnk   1/1     Running   0          92s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP    16h
service/time-app     ClusterIP   10.96.148.153   <none>        8080/TCP   92s
```

## Task 2

- After install with hooks configured(but no hook delete policy):
```
$ kubectl get po
NAME               READY   STATUS      RESTARTS   AGE
postinstall-hook   0/1     Completed   0          33s
preinstall-hook    0/1     Completed   0          58s
```

```
$ kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 12 Nov 2024 10:52:26 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.18
IPs:
  IP:  10.244.0.18
Containers:
  post-install-container:
    Container ID:  docker://6a3aea6dd759c5a3b8b47708e769b9c0df3a1ef540923db08cc2e6e573a0794b
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:768e5c6f5cb6db0794eec98dc7a967f40631746c32232b78a3105fb946f3ab83
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 15
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 12 Nov 2024 10:52:27 +0300
      Finished:     Tue, 12 Nov 2024 10:52:42 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-d8vgt (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-d8vgt:
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
  Normal  Scheduled  83s   default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    83s   kubelet            Pulling image "busybox"
  Normal  Pulled     82s   kubelet            Successfully pulled image "busybox" in 1.312s (1.312s including waiting). Image size: 4042190 bytes.
  Normal  Created    82s   kubelet            Created container post-install-container
  Normal  Started    82s   kubelet            Started container post-install-container
```

```
$ kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 12 Nov 2024 10:52:00 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.17
IPs:
  IP:  10.244.0.17
Containers:
  pre-install-container:
    Container ID:  docker://287b05b866d434e32becc09a2771d09573e62eb81396ff34d66b8af568402216
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:768e5c6f5cb6db0794eec98dc7a967f40631746c32232b78a3105fb946f3ab83
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 12 Nov 2024 10:52:04 +0300
      Finished:     Tue, 12 Nov 2024 10:52:24 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-6qkr2 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-6qkr2:
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
  Normal  Scheduled  2m54s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    2m53s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m50s  kubelet            Successfully pulled image "busybox" in 3.429s (3.429s including waiting). Image size: 4042190 bytes.
  Normal  Created    2m50s  kubelet            Created container pre-install-container
  Normal  Started    2m50s  kubelet            Started container pre-install-container
```
