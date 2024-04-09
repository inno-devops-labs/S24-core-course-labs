# Introduction to Helm

## Task 1: Helm Setup and Chart Creation

### Creating helm `app-python` :

```shell
$ helm create app-python
Creating app-python
```

### Installing chart

```shell
$ helm install app-python  app-python/ --values app-python/values.yaml
NAME: app-python
LAST DEPLOYED: Wed Apr  10 00:31:00 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get --namespace default svc -w app-python'
  export SERVICE_IP=$(kubectl get svc --namespace default app-python --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:5555
```

### Verify by `kubectl get pods,svc` :

```shell
$  kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-687777cd46-28k5p   1/1     Running   0          22s

NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.108.4.166   <pending>     5555:31297/TCP   22s
service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          91s
```

## Task 2: Helm Chart Hooks

### Outputs

```shell
$  kubectl get po
NAME                          READY   STATUS      RESTARTS   AGE
app-python-687777cd46-rb8mq   1/1     Running     0          26s
postinstallhook               0/1     Completed   0          26s
preinstallhook                0/1     Completed   0          34s
```

### Describing pre-install-hook :

```shell
$  kubectl describe po preinstallhook
Name:             preinstallhook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 00:42:09 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
                  helm.sh/hook-delete-policy: hook-succeeded"
Status:           Succeeded
IP:               10.244.0.173
IPs:
  IP:  10.244.0.173
Containers:
  pre-install-container:
    Container ID:  docker://bbe9548f64d5f3a59a827ffb0e6e28af1b0395d6941ab27c812d8165d6369b65
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:6776a33c72b3af7582a5b301e3a08186f2c21a3409f0d2b52dfddbdbe24a5b04
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 5
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 10 Apr 2024 00:42:10 +0300
      Finished:     Wed, 10 Apr 2024 00:42:15 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-c97k4 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-c97k4:
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
  Normal  Scheduled  118s  default-scheduler  Successfully assigned default/preinstallhook to minikube
  Normal  Pulled     118s  kubelet            Container image "busybox" already present on machine
  Normal  Created    118s  kubelet            Created container pre-install-container
  Normal  Started    118s  kubelet            Started container pre-install-container
```

### Describing post-install-hook :

```shell
$  kubectl describe po postinstallhook
Name:             postinstallhook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 00:42:17 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
                  helm.sh/hook-delete-policy: hook-succeeded"
Status:           Succeeded
IP:               10.244.0.175
IPs:
  IP:  10.244.0.175
Containers:
  post-install-container:
    Container ID:  docker://ef05879fb41dd0b6992f6fbc8c34acd878a91a36eab5c49ac1325157521f5dd1
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:6776a33c72b3af7582a5b301e3a08186f2c21a3409f0d2b52dfddbdbe24a5b04
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 5
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 10 Apr 2024 00:42:20 +0300
      Finished:     Wed, 10 Apr 2024 00:42:25 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-58vw2 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-58vw2:
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
  Normal  Scheduled  2m58s  default-scheduler  Successfully assigned default/postinstallhook to minikube
  Normal  Pulling    2m58s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m56s  kubelet            Successfully pulled image "busybox" in 2.418s (2.418s including waiting)
  Normal  Created    2m56s  kubelet            Created container post-install-container
  Normal  Started    2m56s  kubelet            Started container post-install-container
```
