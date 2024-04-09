# Helm

## Helm Setup and Chart Creation
```shell
minikube start --driver=docker
helm install helm-app-python helm-app-python/ --values helm-app-python/values.yaml

Output for `helm install helm-app-python helm-app-python/ --values helm-app-python/values.yaml`

NAME: helm-app-python
LAST DEPLOYED: Wed Apr 10 01:11:12 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get --namespace default svc -w helm-app-python'
  export SERVICE_IP=$(kubectl get svc --namespace default helm-app-python --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:8000

Output for `kubectl get pods,svc`

NAME                                   READY   STATUS    RESTARTS   AGE
pod/helm-app-python-5fc7c7f9c4-gt4rp   1/1     Running   0          47s

NAME                      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/helm-app-python   LoadBalancer   10.103.10.226   <pending>     8000:31338/TCP   48s
service/kubernetes        ClusterIP      10.96.0.1       <none>        443/TCP          62s

```
## Helm Chart Hooks
I added `pre-install-hook.yaml` and `post-install-hook.yaml` for both apps under `templates`. 

### Output(s) **without hook delete policy**.
```shell
NAME: helm-app-python
LAST DEPLOYED: Wed Apr 10 01:17:13 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get --namespace default svc -w helm-app-python'
  export SERVICE_IP=$(kubectl get svc --namespace default helm-app-python --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:8000

NAME                               READY   STATUS      RESTARTS   AGE
helm-app-python-5fc7c7f9c4-zjx7t   1/1     Running     0          89s
postinstall-hook                   0/1     Completed   0          89s
preinstall-hook                    0/1     Completed   0          118s

```
```shell
kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 01:17:14 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.3
IPs:
  IP:  10.244.0.3
Containers:
  pre-install-container:
    Container ID:  docker://6eceef4fee0edd8f51ae6a060fe29b41ed6561ec8885e23c008da83f09093250
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
      Started:      Wed, 10 Apr 2024 01:17:21 +0300
      Finished:     Wed, 10 Apr 2024 01:17:41 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-tmnc4 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-tmnc4:
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
  Normal  Scheduled  2m14s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    2m14s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m7s   kubelet            Successfully pulled image "busybox" in 6.608s (6.608s including waiting)
  Normal  Created    2m7s   kubelet            Created container pre-install-container
  Normal  Started    2m7s   kubelet            Started container pre-install-container

```
```shell
kubectl describe po postinstall-hookName:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 01:17:43 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.5
IPs:
  IP:  10.244.0.5
Containers:
  post-install-container:
    Container ID:  docker://32a9bb4a2f1f46ce257cdd9bbdaa1e1cfe8605109ab46e484899128ab00f9295
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 10 Apr 2024 01:18:07 +0300
      Finished:     Wed, 10 Apr 2024 01:18:27 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-9qt62 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-9qt62:
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
  Normal  Scheduled  2m38s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    2m37s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m14s  kubelet            Successfully pulled image "busybox" in 3.202s (23.472s including waiting)
  Normal  Created    2m14s  kubelet            Created container post-install-container
  Normal  Started    2m14s  kubelet            Started container post-install-container
```
```shell
kubectl get pods,svc
NAME                                   READY   STATUS      RESTARTS   AGE
pod/helm-app-python-5fc7c7f9c4-zjx7t   1/1     Running     0          3m15s
pod/postinstall-hook                   0/1     Completed   0          3m15s
pod/preinstall-hook                    0/1     Completed   0          3m44s

NAME                      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/helm-app-python   LoadBalancer   10.96.118.214   <pending>     8000:30256/TCP   3m15s
service/kubernetes        ClusterIP      10.96.0.1       <none>        443/TCP          6m24s

```
### Viewing the labels from `minikube dashboard`
[![image.png](https://i.postimg.cc/GtbmfgXN/image.png)](https://postimg.cc/TLHxL0Mq)