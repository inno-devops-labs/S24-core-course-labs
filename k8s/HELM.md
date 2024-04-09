# Helm

## Basic Helm Chart

```bash
(venv) PS C:\Users\smash\PyCharmProjects\S24-core-course-labs\k8s> kubectl get pods,svc

NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-94656cff8-9bpbj   1/1     Running   0          81s
pod/app-python-94656cff8-xp26b   1/1     Running   0          81s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.100.198.50   <pending>     8080:31371/TCP   81s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          6d19h
```

## Helm Chart with pre- and post- install hooks

```bash
(venv) PS C:\Users\smash\PyCharmProjects\S24-core-course-labs\k8s> kubectl get pods,svc

NAME                                         READY   STATUS      RESTARTS   AGE
pod/helm-hooks-app-python-65f6cbc4cf-2dbtd   1/1     Running     0          30s
pod/helm-hooks-app-python-65f6cbc4cf-bc5rd   1/1     Running     0          30s
pod/post-install-hook                        0/1     Completed   0          30s
pod/pre-install-hook                         0/1     Completed   0          43s

NAME                            TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/helm-hooks-app-python   LoadBalancer   10.98.30.171   <pending>     8080:31297/TCP   30s
service/kubernetes              ClusterIP      10.96.0.1      <none>        443/TCP          6d19h
```

```bash
(venv) PS C:\Users\smash\PyCharmProjects\S24-core-course-labs\k8s> kubectl get po

NAME                                     READY   STATUS      RESTARTS   AGE
helm-hooks-app-python-65f6cbc4cf-2dbtd   1/1     Running     0          64s
helm-hooks-app-python-65f6cbc4cf-bc5rd   1/1     Running     0          64s
post-install-hook                        0/1     Completed   0          64s
pre-install-hook                         0/1     Completed   0          77s
```

```bash
(venv) PS C:\Users\smash\PyCharmProjects\S24-core-course-labs\k8s> kubectl describe po pre-install-hook     

Name:             pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 19:08:20 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.27
IPs:
  IP:  10.244.0.27
Containers:
  sleep-5:
    Container ID:  docker://260a7964f6d1a27597bc41030375352b35a587ddf0446d7f77d0fc1e9874f542
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sleep
    Args:
      5
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 09 Apr 2024 19:08:26 +0300
      Finished:     Tue, 09 Apr 2024 19:08:31 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-wsxzz (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-wsxzz:
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
  Normal  Scheduled  117s  default-scheduler  Successfully assigned default/pre-install-hook to minikube
  Normal  Pulling    117s  kubelet            Pulling image "busybox"
  Normal  Pulled     112s  kubelet            Successfully pulled image "busybox" in 5.254s (5.254s including waiting)
  Normal  Created    112s  kubelet            Created container sleep-5
  Normal  Started    112s  kubelet            Started container sleep-5
```

```bash
(venv) PS C:\Users\smash\PyCharmProjects\S24-core-course-labs\k8s> kubectl describe po post-install-hook

Name:             post-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 19:08:33 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.30
IPs:
  IP:  10.244.0.30
Containers:
  sleep-10:
    Container ID:  docker://85472c69b9f1a7666e129bfa7efc7bbc2652b491b677255ee33d6d309128d6d6
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sleep
    Args:
      10
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 09 Apr 2024 19:08:35 +0300
      Finished:     Tue, 09 Apr 2024 19:08:45 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-pb696 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-pb696:
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
  Normal  Scheduled  2m23s  default-scheduler  Successfully assigned default/post-install-hook to minikube
  Normal  Pulling    2m22s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m21s  kubelet            Successfully pulled image "busybox" in 1.575s (1.575s including waiting)
  Normal  Created    2m21s  kubelet            Created container sleep-10
  Normal  Started    2m21s  kubelet            Started container sleep-10
```