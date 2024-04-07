# Helm
### 1st task
Installing helm chart:
`helm install app-python app-python`

```
NAME: app-python
LAST DEPLOYED: Sun Apr  7 17:36:41 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services app-python)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
```

Running minikube dashboard to verify that the serivce is healthy:
`minikube dashboard`
![Screenshot from 2024-04-07 17-46-30.png](images%2FScreenshot%20from%202024-04-07%2017-46-30.png)

Access the application via curl:
```
djovi@djovi-NBD-WXX9:~/PycharmProjects/S24-core-course-labs/k8s$ minikube service app-python
|-----------|------------|-------------|----------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL             |
|-----------|------------|-------------|----------------------------|
| default   | app-python | http/5000   | http://192.168.148.2:30980 |
|-----------|------------|-------------|----------------------------|
🎉  Opening service default/app-python in default browser...
curl http://192.168.148.2:30980/

The current time in Moscow is: 2024-04-07 17:39:32
```
Verify the deployment:
`kubectl get pods,svc`
```
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-5b6bdb64f9-4m7qd   1/1     Running   0          3m19s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   NodePort    10.100.164.22   <none>        5000:30980/TCP   3m19s
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          9d
```
## Helm Chart Hooks
Lint the Helm chart
```
helm lint app-python/
==> Linting app-python/
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```
Perform dry-run of the Helm chart (output is truncated)
```
NAME: helm-hooks
LAST DEPLOYED: Sun Apr  7 18:09:43 2024
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:

# Source: app-python/templates/post-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
  name: postinstall-hook
  annotations:
    "helm.sh/hook": "post-install"
```
Verify the Helm chart hooks (without hook delete policy)
`kubectl get po`
```
NAME                          READY   STATUS      RESTARTS   AGE
app-python-5b6bdb64f9-9k2x6   1/1     Running     0          40s
postinstall-hook              0/1     Completed   0          40s
preinstall-hook               0/1     Completed   0          62s
```
`kubectl describe po preinstall-hook`
```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.148.2
Start Time:       Sun, 07 Apr 2024 19:09:07 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.59
IPs:
  IP:  10.244.0.59
Containers:
  pre-install-container:
    Container ID:  docker://31698cca031de339a43f7f1e4db58e5e4154c905da2b00bf070bbc0deef33d5d
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
      Started:      Sun, 07 Apr 2024 19:09:07 +0300
      Finished:     Sun, 07 Apr 2024 19:09:27 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-lpz4q (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-lpz4q:
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
  Normal  Scheduled  103s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     103s  kubelet            Container image "busybox" already present on machine
  Normal  Created    103s  kubelet            Created container pre-install-container
  Normal  Started    103s  kubelet            Started container pre-install-container
```
`kubectl describe po postinstall-hook`
```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.148.2
Start Time:       Sun, 07 Apr 2024 19:09:07 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.59
IPs:
  IP:  10.244.0.59
Containers:
  pre-install-container:
    Container ID:  docker://31698cca031de339a43f7f1e4db58e5e4154c905da2b00bf070bbc0deef33d5d
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
      Started:      Sun, 07 Apr 2024 19:09:07 +0300
      Finished:     Sun, 07 Apr 2024 19:09:27 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-lpz4q (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-lpz4q:
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
  Normal  Scheduled  103s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     103s  kubelet            Container image "busybox" already present on machine
  Normal  Created    103s  kubelet            Created container pre-install-container
  Normal  Started    103s  kubelet            Started container pre-install-container
```
Verify that only the application pod in running after enabling the hook delete policy
`kubectl get pods,svc`
```
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-5b6bdb64f9-sn49r   1/1     Running   0          59s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   NodePort    10.96.105.116   <none>        5000:30308/TCP   59s
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          9d
```