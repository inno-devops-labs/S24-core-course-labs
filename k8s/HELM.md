# Helm

## `kubectl get pods,svc` output with `app-python` chart

```shell
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-7df5ddcb5b-9l4pm   1/1     Running   0          3m10s

NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/app-python   ClusterIP   10.110.225.3   <none>        8080/TCP   3m10s
service/kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP    25h
```

## `kubectl get po` output

```shell
$ kubectl get po
NAME                           READY   STATUS      RESTARTS   AGE
app-python-7df5ddcb5b-x2dbg    1/1     Running     0          86s
app-python-postinstall-p5f94   0/1     Completed   0          86s
app-python-preinstall-jgjcq    0/1     Completed   0          110s
```

## `kubectl describe po app-python-preinstall` output

```shell
$ kubectl describe po app-python-preinstall
Name:             app-python-preinstall-jgjcq
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Thu, 21 Mar 2024 12:00:20 +0300
Labels:           app.kubernetes.io/instance=app-python
                  app.kubernetes.io/managed-by=Helm
                  batch.kubernetes.io/controller-uid=56fd6360-d206-4480-b24a-5b2b472bd1b5
                  batch.kubernetes.io/job-name=app-python-preinstall
                  controller-uid=56fd6360-d206-4480-b24a-5b2b472bd1b5
                  helm.sh/chart=app-python-0.1.0
                  job-name=app-python-preinstall
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.57
IPs:
  IP:           10.244.0.57
Controlled By:  Job/app-python-preinstall
Containers:
  post-install-job:
    Container ID:  docker://2b6bc02d6a7812ea3ce8bb27753f80153eb7f567807eaf5b272189b1cb859879
    Image:         alpine:3.3
    Image ID:      docker-pullable://alpine@sha256:6bff6f65597a69246f79233ef37ff0dc50d97eaecbabbe4f8a885bf358be1ecf
    Port:          <none>
    Host Port:     <none>
    Command:
      /bin/sleep
      20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Thu, 21 Mar 2024 12:00:21 +0300
      Finished:     Thu, 21 Mar 2024 12:00:41 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-btq2k (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-btq2k:
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
  Normal  Scheduled  65s   default-scheduler  Successfully assigned default/app-python-preinstall-jgjcq to minikube
  Normal  Pulled     64s   kubelet            Container image "alpine:3.3" already present on machine
  Normal  Created    64s   kubelet            Created container post-install-job
  Normal  Started    64s   kubelet            Started container post-install-job
```

## `kubectl describe po app-python-postinstall` output

```shell
$ kubectl describe po app-python-postinstall
Name:             app-python-postinstall-p5f94
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Thu, 21 Mar 2024 12:00:44 +0300
Labels:           app.kubernetes.io/instance=app-python
                  app.kubernetes.io/managed-by=Helm
                  batch.kubernetes.io/controller-uid=df058c96-3748-4aae-9abc-39a2bc1fefe0
                  batch.kubernetes.io/job-name=app-python-postinstall
                  controller-uid=df058c96-3748-4aae-9abc-39a2bc1fefe0
                  helm.sh/chart=app-python-0.1.0
                  job-name=app-python-postinstall
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.58
IPs:
  IP:           10.244.0.58
Controlled By:  Job/app-python-postinstall
Containers:
  post-install-job:
    Container ID:  docker://2fdd7a6f9a5584ffacb89a383c4f41f991b3687e8d6ecc5b93f10f3f7ce403f0
    Image:         alpine:3.3
    Image ID:      docker-pullable://alpine@sha256:6bff6f65597a69246f79233ef37ff0dc50d97eaecbabbe4f8a885bf358be1ecf
    Port:          <none>
    Host Port:     <none>
    Command:
      /bin/sleep
      20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Thu, 21 Mar 2024 12:00:47 +0300
      Finished:     Thu, 21 Mar 2024 12:01:07 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-6gczx (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-6gczx:
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
  Normal  Scheduled  3m14s  default-scheduler  Successfully assigned default/app-python-postinstall-p5f94 to minikube
  Normal  Pulled     3m11s  kubelet            Container image "alpine:3.3" already present on machine
  Normal  Created    3m11s  kubelet            Created container post-install-job
  Normal  Started    3m11s  kubelet            Started container post-install-job
```