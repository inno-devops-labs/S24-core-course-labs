`kubectl get pods,svc`
```
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-59f77d75b7-r2wwj   1/1     Running   0          42m

NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
service/app-python   ClusterIP   10.110.67.53   <none>        80/TCP    42m
service/kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP   9d
```

`helm lint app-python`
```
==> Linting app-python
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

`helm install --dry-run helm-hooks app-python`
```
NAME: helm-hooks
LAST DEPLOYED: Tue Apr  9 22:31:58 2024
NAMESPACE: default
STATUS: pending-install
REVISION: 1
TEST SUITE: None
HOOKS:
---
# Source: app-python/templates/post-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
   name: postinstall-hook
   annotations:
       "helm.sh/hook": "post-install"
       "helm.sh/hook-delete-policy": hook-succeeded
spec:
  containers:
  - name: post-install-container
    image: busybox
    imagePullPolicy: Always
    command: ['sh', '-c', 'echo The post-install hook is running && sleep 15' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---
# Source: app-python/templates/pre-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
   name: preinstall-hook
   annotations:
       "helm.sh/hook": "pre-install"
       "helm.sh/hook-delete-policy": hook-succeeded
spec:
  containers:
  - name: pre-install-container
    image: busybox
    imagePullPolicy: IfNotPresent
    command: ['sh', '-c', 'echo The pre-install hook is running && sleep 20' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
MANIFEST:
---
# Source: app-python/templates/statefulset.yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: app-python
spec:
  serviceName: app-python-service
  replicas: 1
  selector:
    matchLabels:
      app: app-python
  template:
    metadata:
      labels:
        app: app-python
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: app-python
        image: catdog905/dev-ops-course-app-python
        imagePullPolicy: Always
```

`kubectl get po`
```
NAME                          READY   STATUS             RESTARTS   AGE
app-python-59f77d75b7-r2wwj   1/1     Running            0          66m
preinstall-hook               0/1     ImagePullBackOff   0          11m
```

`kubectl describe po preinstall-hook`
```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 22:21:57 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Pending
IP:               10.244.0.34
IPs:
  IP:  10.244.0.34
Containers:
  pre-install-container:
    Container ID:  
    Image:         busybox
    Image ID:      
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Waiting
      Reason:       ImagePullBackOff
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-txv85 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-txv85:
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
  Normal   Scheduled  12m                   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Warning  Failed     10m (x3 over 12m)     kubelet            Failed to pull image "busybox": Error response from daemon: Get "https://registry-1.docker.io/v2/": dial tcp: lookup registry-1.docker.io on 192.168.49.1:53: server misbehaving
  Normal   Pulling    10m (x4 over 12m)     kubelet            Pulling image "busybox"
  Warning  Failed     9m51s (x4 over 12m)   kubelet            Error: ErrImagePull
  Warning  Failed     9m51s                 kubelet            Failed to pull image "busybox": Error response from daemon: Head "https://registry-1.docker.io/v2/library/busybox/manifests/latest": Get "https://auth.docker.io/token?scope=repository%3Alibrary%2Fbusybox%3Apull&service=registry.docker.io": dial tcp: lookup auth.docker.io on 192.168.49.1:53: server misbehaving
  Warning  Failed     9m26s (x6 over 12m)   kubelet            Error: ImagePullBackOff
  Normal   BackOff    2m11s (x35 over 12m)  kubelet            Back-off pulling image "busybox"
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 22:21:57 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Pending
IP:               10.244.0.34
IPs:
  IP:  10.244.0.34
Containers:
  pre-install-container:
    Container ID:  
    Image:         busybox
    Image ID:      
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Waiting
      Reason:       ImagePullBackOff
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-txv85 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-txv85:
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
  Normal   Scheduled  12m                   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Warning  Failed     11m (x3 over 12m)     kubelet            Failed to pull image "busybox": Error response from daemon: Get "https://registry-1.docker.io/v2/": dial tcp: lookup registry-1.docker.io on 192.168.49.1:53: server misbehaving
  Normal   Pulling    10m (x4 over 12m)     kubelet            Pulling image "busybox"
  Warning  Failed     9m54s (x4 over 12m)   kubelet            Error: ErrImagePull
  Warning  Failed     9m54s                 kubelet            Failed to pull image "busybox": Error response from daemon: Head "https://registry-1.docker.io/v2/library/busybox/manifests/latest": Get "https://auth.docker.io/token?scope=repository%3Alibrary%2Fbusybox%3Apull&service=registry.docker.io": dial tcp: lookup auth.docker.io on 192.168.49.1:53: server misbehaving
  Warning  Failed     9m29s (x6 over 12m)   kubelet            Error: ImagePullBackOff
  Normal   BackOff    2m14s (x35 over 12m)  kubelet            Back-off pulling image "busybox"
```
