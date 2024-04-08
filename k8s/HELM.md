# Task 1

## `kubectl get pods,svc`

```bash
NAME                            READY   STATUS    RESTARTS   AGE
pod/flask-app-c7f894c9b-8w7vn   1/1     Running   0          2m7s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
service/flask-app    ClusterIP   10.101.134.153   <none>        80/TCP    2m7s
service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP   21h
```

# Task 2

## `kubectl get po`

```bash
NAME                         READY   STATUS      RESTARTS      AGE
flask-app-85c56c98bc-xpnlm   0/1     Running     4 (24s ago)   2m24s
postinstall-hook             0/1     Completed   0             2m24s
preinstall-hook              0/1     Completed   0             2m37s
```

## `kubectl describe po preinstall-hook`

```bash
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Mon, 08 Apr 2024 23:34:41 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.50
IPs:
  IP:  10.244.0.50
Containers:
  pre-install-container:
    Container ID:  docker://e46d49807dada4e936d23f68bad991c780f4a339f7737b1ebcbdd48b8604f938
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo preinstall hook && sleep 10
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Mon, 08 Apr 2024 23:34:42 +0300
      Finished:     Mon, 08 Apr 2024 23:34:52 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-xpfd2 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-xpfd2:
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
  Normal  Scheduled  4m3s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     4m3s  kubelet            Container image "busybox" already present on machine
  Normal  Created    4m3s  kubelet            Created container pre-install-container
  Normal  Started    4m3s  kubelet            Started container pre-install-container
```

## `kubectl describe po postinstall-hook`

```bash
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Mon, 08 Apr 2024 23:34:54 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.52
IPs:
  IP:  10.244.0.52
Containers:
  post-install-container:
    Container ID:  docker://fdb9aee647732692c7903545570aa8a2183a129a6b37efabe5e2bf2f7185d448
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo postinstall hook && sleep 10
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Mon, 08 Apr 2024 23:35:25 +0300
      Finished:     Mon, 08 Apr 2024 23:35:35 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-scwqh (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-scwqh:
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
  Normal  Scheduled  5m4s   default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    5m4s   kubelet            Pulling image "busybox"
  Normal  Pulled     4m33s  kubelet            Successfully pulled image "busybox" in 30.146s (30.146s including waiting)
  Normal  Created    4m33s  kubelet            Created container post-install-container
  Normal  Started    4m33s  kubelet            Started container post-install-container
```