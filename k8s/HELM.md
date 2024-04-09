# Setup

To install, I use `helm install web-app ./web-app/ --values ./web-app/values.yaml`

# Confirm

To confirm the success, I use ` minikube kubectl get pods,svc` and see

```shell
NAME                           READY   STATUS    RESTARTS   AGE
pod/web-app-84cc4bdd9c-shjh9   1/1     Running   0          9s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   6d23h
service/web-app      ClusterIP   10.96.162.147   <none>        80/TCP    9s
```

# Hooks

`kubectl get po` during preinstall:

```shell
NAME              READY   STATUS    RESTARTS   AGE
preinstall-hook   1/1     Running   0          2s
```

`kubectl get po` during postinstall:

```shell
NAME                       READY   STATUS    RESTARTS   AGE
postinstall-hook           1/1     Running   0          14s
web-app-84cc4bdd9c-pk5nj   1/1     Running   0          14s
```

`kubectl get po` after postinstall:

```shell
NAME                       READY   STATUS    RESTARTS   AGE
web-app-84cc4bdd9c-s6gqt   1/1     Running   0          16s
```

`minikube kubectl describe po preinstall-hook`:

```shell
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 00:45:52 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
                  helm.sh/hook-delete-policy: hook-succeeded
Status:           Running
IP:               10.244.0.34
IPs:
  IP:  10.244.0.34
Containers:
  pre-install-container:
    Container ID:  docker://c0f2ceb305b0dda51ba493ccef1fc982a776a86fe6286102169a84670675c736
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 10
    State:          Running
      Started:      Wed, 10 Apr 2024 00:45:53 +0300
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-whqkr (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-whqkr:
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
  Normal  Scheduled  2s    default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     1s    kubelet            Container image "busybox" already present on machine
  Normal  Created    1s    kubelet            Created container pre-install-container
  Normal  Started    1s    kubelet            Started container pre-install-container
```



`minikube kubectl describe po preinstall-hook`:

```shell
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 00:46:06 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
                  helm.sh/hook-delete-policy: hook-succeeded
Status:           Running
IP:               10.244.0.36
IPs:
  IP:  10.244.0.36
Containers:
  post-install-container:
    Container ID:  docker://957a9b767ae42f45b10814fb6ca7a07e7a379677c0820c78e6b410a7c6e00760
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 10
    State:          Running
      Started:      Wed, 10 Apr 2024 00:46:10 +0300
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-6c5kk (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-6c5kk:
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
  Normal  Scheduled  8s    default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    7s    kubelet            Pulling image "busybox"
  Normal  Pulled     5s    kubelet            Successfully pulled image "busybox" in 2.441s (2.441s including waiting)
  Normal  Created    5s    kubelet            Created container post-install-container
  Normal  Started    4s    kubelet            Started container post-install-container
```

