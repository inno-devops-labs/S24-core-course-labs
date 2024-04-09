# Task 1
## Command
```bash
kubectl get pods,svc
```
## Output
```bash
NAME                             READY   STATUS    RESTARTS   AGE
pod/flask-app-767b4b7cc6-w48dg   1/1     Running   0          8s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/flask-app    ClusterIP   10.105.140.121   <none>        5000/TCP   8s
service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP    6d23h
```
# Task 2
## 2.4.*a*
### Command
```bash
kubectl get po
```
### Output
```bash
helm-hooks-flask-app-68545757b4-sjgpz   1/1     Running     0          5m27s
postinstall-hook                        0/1     Completed   0          5m27s
preinstall-hook                         0/1     Completed   0          5m49s
```
## 2.4.*b*
### Command
```bash
kubectl describe po preinstall-hook 
```
### Output
```bash
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 23:13:45 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.36
IPs:
  IP:  10.244.0.36
Containers:
  pre-install-container:
    Container ID:  docker://c226cf8b46e28e32fa85a36b93715f0bdd1e71bae2587481e8c33b0516fe1b5c
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 09 Apr 2024 23:13:46 +0300
      Finished:     Tue, 09 Apr 2024 23:14:06 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-vpcmc (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-vpcmc:
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
  Normal  Scheduled  6m23s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     6m22s  kubelet            Container image "busybox" already present on machine
  Normal  Created    6m22s  kubelet            Created container pre-install-container
  Normal  Started    6m22s  kubelet            Started container pre-install-container
```
## 2.4.*c*
### Command
```bash
kubectl describe po postinstall-hook 
```
### Output
```bash
Name:             postinstall-hook               
Namespace:        default                        
Priority:         0                              
Service Account:  default                        
Node:             minikube/192.168.49.2          
Start Time:       Tue, 09 Apr 2024 23:14:07 +0300
Labels:           <none>                         
Annotations:      helm.sh/hook: post-install     
Status:           Succeeded
IP:               10.244.0.38
IPs:
  IP:  10.244.0.38
Containers:
  post-install-container:
    Container ID:  docker://d8212b5e351f7142bc695ba7e5af5e54b768cc37e192f62f75adf5a74e04eaf7
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 15
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 09 Apr 2024 23:14:10 +0300
      Finished:     Tue, 09 Apr 2024 23:14:25 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-8qkhw (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-8qkhw:
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
  Normal  Scheduled  6m44s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    6m44s  kubelet            Pulling image "busybox"
  Normal  Pulled     6m42s  kubelet            Successfully pulled image "busybox" in 1.938s (1.938s including waiting)
  Normal  Created    6m42s  kubelet            Created container post-install-container
  Normal  Started    6m42s  kubelet            Started container post-install-container
```