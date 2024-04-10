# Lab 10 (Helm)

## Task 1

```bash
§ kubectl get pods,svc
NAME                               READY   STATUS    RESTARTS   AGE
pod/moscow-time-74cd84f7d8-sf7t8   1/1     Running   0          4m15s

NAME                  TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/kubernetes    ClusterIP   10.96.0.1       <none>        443/TCP    7d9h
service/moscow-time   ClusterIP   10.101.248.33   <none>        8000/TCP   4m15s
```

## Task 2

```bash
§ kubectl get po
NAME                                 READY   STATUS      RESTARTS   AGE
moscow-time-74cd84f7d8-h4f47         1/1     Running     0          32s
moscow-time-postinstall-hook-mc66g   0/1     Completed   0          32s
moscow-time-preinstall-hook-w4kcg    0/1     Completed   0          46s
iu_devops/k8s on  lab9 [?]
§ kubectl describe po moscow-time-preinstall-hook-w4kcg
Name:             moscow-time-preinstall-hook-w4kcg
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 08:51:21 +0300
Labels:           app.kubernetes.io/instance=moscow-time
                  app.kubernetes.io/managed-by=Helm
                  batch.kubernetes.io/controller-uid=780a41c4-c05c-4d80-b955-bedc295d3a3a
                  batch.kubernetes.io/job-name=moscow-time-preinstall-hook
                  controller-uid=780a41c4-c05c-4d80-b955-bedc295d3a3a
                  helm.sh/chart=moscow-time-0.1.0
                  job-name=moscow-time-preinstall-hook
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.36
IPs:
  IP:           10.244.0.36
Controlled By:  Job/moscow-time-preinstall-hook
Containers:
  pre-install-job:
    Container ID:  docker://16d42cd32288e6b01b82c323fd8f4f0d3151f49eac9ed62b883ad6771a7ccd1a
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 10
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 10 Apr 2024 08:51:22 +0300
      Finished:     Wed, 10 Apr 2024 08:51:32 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-6wwtt (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-6wwtt:
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
  Normal  Scheduled  64s   default-scheduler  Successfully assigned default/moscow-time-preinstall-hook-w4kcg to minikube
  Normal  Pulled     64s   kubelet            Container image "busybox" already present on machine
  Normal  Created    64s   kubelet            Created container pre-install-job
  Normal  Started    64s   kubelet            Started container pre-install-job
iu_devops/k8s on  lab9 [?]
§ kubectl describe po moscow-time-postinstall-hook-mc66g
Name:             moscow-time-postinstall-hook-mc66g
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 08:51:35 +0300
Labels:           app.kubernetes.io/instance=moscow-time
                  app.kubernetes.io/managed-by=Helm
                  batch.kubernetes.io/controller-uid=0cf0a4a6-5f5c-40ac-a64f-b20ccd4cec49
                  batch.kubernetes.io/job-name=moscow-time-postinstall-hook
                  controller-uid=0cf0a4a6-5f5c-40ac-a64f-b20ccd4cec49
                  helm.sh/chart=moscow-time-0.1.0
                  job-name=moscow-time-postinstall-hook
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.38
IPs:
  IP:           10.244.0.38
Controlled By:  Job/moscow-time-postinstall-hook
Containers:
  post-install-job:
    Container ID:  docker://d7f9d6f63363d655a8f8b1f1026b0efb88a4f19ea74cf4d0d89b7c4e8fa4d6f9
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 10
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 10 Apr 2024 08:51:35 +0300
      Finished:     Wed, 10 Apr 2024 08:51:45 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-prscz (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-prscz:
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
  Normal  Scheduled  58s   default-scheduler  Successfully assigned default/moscow-time-postinstall-hook-mc66g to minikube
  Normal  Pulled     58s   kubelet            Container image "busybox" already present on machine
  Normal  Created    58s   kubelet            Created container post-install-job
  Normal  Started    58s   kubelet            Started container post-install-job
```

```bash
§ kubectl get pods,svc
NAME                                     READY   STATUS      RESTARTS   AGE
pod/moscow-time-74cd84f7d8-h4f47         1/1     Running     0          108s
pod/moscow-time-postinstall-hook-mc66g   0/1     Completed   0          108s
pod/moscow-time-preinstall-hook-w4kcg    0/1     Completed   0          2m2s

NAME                  TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/kubernetes    ClusterIP   10.96.0.1        <none>        443/TCP    2m46s
service/moscow-time   ClusterIP   10.111.239.156   <none>        8000/TCP   108s
```
