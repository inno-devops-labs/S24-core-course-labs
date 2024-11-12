# Helm lab command outputs

## kubectl get pod,svc

Note that it was run before hooks were added. All other commands are run after I added the hooks.

```
NAME                                 READY   STATUS      RESTARTS   AGE
pod/time-server-57d7976c86-8mzp4     1/1     Running     0          46s

NAME                  TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/kubernetes    ClusterIP   10.96.0.1       <none>        443/TCP    45m
service/time-server   ClusterIP   10.100.44.128   <none>        5000/TCP   46s
```

## kubectl get po

```
NAME                             READY   STATUS      RESTARTS   AGE
time-server-57d7976c86-8mzp4     1/1     Running     0          114s
time-server-post-install-tsf6p   0/1     Completed   0          114s
time-server-pre-install-w8lzd    0/1     Completed   0          2m7s
```

## kubectl describe po time-server-pre-install-w8lzd

```
Name:             time-server-pre-install-w8lzd
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 12 Nov 2024 01:15:42 +0500
Labels:           app.kubernetes.io/instance=time-server
                  app.kubernetes.io/managed-by=Helm
                  batch.kubernetes.io/controller-uid=f9651627-6e98-40fe-b2ed-7786a7652fac
                  batch.kubernetes.io/job-name=time-server-pre-install
                  controller-uid=f9651627-6e98-40fe-b2ed-7786a7652fac
                  helm.sh/chart=time-server-0.1.0
                  job-name=time-server-pre-install
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.21
IPs:
  IP:           10.244.0.21
Controlled By:  Job/time-server-pre-install
Containers:
  pre-install-job:
    Container ID:  docker://2149cf70a0cbb9b04ad940ad942d44d26cbeedc0692fb6536d49179bde4197f7
    Image:         alpine:3.3
    Image ID:      docker-pullable://alpine@sha256:6bff6f65597a69246f79233ef37ff0dc50d97eaecbabbe4f8a885bf358be1ecf
    Port:          <none>
    Host Port:     <none>
    Command:
      /bin/sleep
      10
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 12 Nov 2024 01:15:43 +0500
      Finished:     Tue, 12 Nov 2024 01:15:53 +0500
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-2hfc9 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-2hfc9:
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
  Normal  Scheduled  3m31s  default-scheduler  Successfully assigned default/time-server-pre-install-w8lzd to minikube
  Normal  Pulled     3m30s  kubelet            Container image "alpine:3.3" already present on machine
  Normal  Created    3m30s  kubelet            Created container pre-install-job
  Normal  Started    3m30s  kubelet            Started container pre-install-job
```

## kubectl describe po time-server-post-install-tsf6p

```
Name:             time-server-post-install-tsf6p
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 12 Nov 2024 01:15:55 +0500
Labels:           app.kubernetes.io/instance=time-server
                  app.kubernetes.io/managed-by=Helm
                  batch.kubernetes.io/controller-uid=ae0aab79-ab62-4f8b-8b29-b96e90bcaf97
                  batch.kubernetes.io/job-name=time-server-post-install
                  controller-uid=ae0aab79-ab62-4f8b-8b29-b96e90bcaf97
                  helm.sh/chart=time-server-0.1.0
                  job-name=time-server-post-install
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.23
IPs:
  IP:           10.244.0.23
Controlled By:  Job/time-server-post-install
Containers:
  post-install-job:
    Container ID:  docker://a9abab049dff5aa57cb82831cf3da82aa61955e0072c7496fa80c5f58f446d9b
    Image:         alpine:3.3
    Image ID:      docker-pullable://alpine@sha256:6bff6f65597a69246f79233ef37ff0dc50d97eaecbabbe4f8a885bf358be1ecf
    Port:          <none>
    Host Port:     <none>
    Command:
      /bin/sleep
      10
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 12 Nov 2024 01:15:57 +0500
      Finished:     Tue, 12 Nov 2024 01:16:07 +0500
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-kt2gs (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  kube-api-access-kt2gs:
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
  Normal  Scheduled  4m10s  default-scheduler  Successfully assigned default/time-server-post-install-tsf6p to minikube
  Normal  Pulled     4m8s   kubelet            Container image "alpine:3.3" already present on machine
  Normal  Created    4m8s   kubelet            Created container post-install-job
  Normal  Started    4m8s   kubelet            Started container post-install-job
```

