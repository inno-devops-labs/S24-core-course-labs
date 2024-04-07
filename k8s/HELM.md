# Helm Outputs
### Output of the command `kubectl get pods,svc`

```shell
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-43c3d12arp-zxfkj   1/1     Running   0          7m54s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.109.130.162  <pending>     5000:30898/TCP   7m54s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          6d12h
```
### Output of the command `kubectl get po`
```shell
NAME                          READY   STATUS      RESTARTS   AGE
app-python-24d6c34ses-wxpaz   1/1     Running     0          8m31s
postinstall-hook              0/1     Completed   0          8m31s
preinstall-hook               0/1     Completed   0          8m54s
```

### Output of the command `kubectl describe po preinstall-hook`
```shell
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 07 Apr 2024 18:31:15 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.24
IPs:
  IP:  10.244.0.24
Containers:
  pre-install-container:
    Container ID:  docker://6er2r8c2385rf4hp4246nw75gw410vs4rg275fq3493425d0e3y9636ae09242e3
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3efd24174424a6d997e74f52b878d7cf26824yfseac6bs472eesfe21a7w1w42
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 07 Apr 2024 18:31:15 +0300
      Finished:     Sun, 07 Apr 2024 18:51:15 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-tz9n2 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-tz9n2:
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
  Normal  Scheduled  3m26s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     3m25s  kubelet            Container image "busybox" already present on machine
  Normal  Created    3m25s  kubelet            Created container pre-install-container
  Normal  Started    3m25s  kubelet            Started container pre-install-container
```

### Output of the command `kubectl describe po postinstall-hook`
```shell
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 07 Apr 2024 18:31:15 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.26
IPs:
  IP:  10.244.0.26
Containers:
  post-install-container:
    Container ID:  docker://s327g38g00843c58a62v3949ffe2fr9f6b03eb7d8f30b8g2e81dp45917659f5m
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:4dbc732461424r7s937e54l53b858d5cf478525pfsag6bc957ekdew51s7f5e75
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 15
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 07 Apr 2024 18:31:15 +0300
      Finished:     Sun, 07 Apr 2024 18:51:26 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-ztcs2 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-ztcs2:
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
  Type     Reason     Age                   From               Message
  ----     ------     ----                  ----               -------
  Normal   Scheduled  4m12s                 default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal   Pulling    3m4s (x3 over 4m11s)  kubelet            Pulling image "busybox"
  Normal   Pulled     3m1s                  kubelet            Successfully pulled image "busybox" in 2.397094385s (2.397127049s including waiting)  
  Normal   Created    3m1s                  kubelet            Created container post-install-container
  Normal   Started    3m1s                  kubelet            Started container post-install-container
```