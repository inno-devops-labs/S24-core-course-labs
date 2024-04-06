## Task 1

```bash
$ helm install my-helm-app-python helm-app-python/ --values helm-app-python/values.yaml

NAME: my-helm-app-python
LAST DEPLOYED: Sat Apr  6 14:39:07 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get --namespace default svc -w my-helm-app-python'
  export SERVICE_IP=$(kubectl get svc --namespace default my-helm-app-python --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:8080

$ helm install my-helm-app-go helm-app-go/ --values helm-app-go/values.yaml
# ....
```



```bash
$ kubectl get pods,svc

NAME                                      READY   STATUS    RESTARTS   AGE
pod/my-helm-app-go-85c945559-85sgg        1/1     Running   0          103s
pod/my-helm-app-python-86f7dfdcc9-49z6j   1/1     Running   0          14s

NAME                         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes           ClusterIP      10.96.0.1       <none>        443/TCP          37m
service/my-helm-app-go       LoadBalancer   10.105.61.204   <pending>     8080:32616/TCP   103s
service/my-helm-app-python   LoadBalancer   10.99.60.12     <pending>     8080:30201/TCP   14s
```



## Task 2

```bash
$ helm install my-helm-app-python helm-app-python/ --values helm-app-python/values.yaml
```

```bash
$ kubectl get po
NAME                                  READY   STATUS      RESTARTS   AGE
my-helm-app-python-86f7dfdcc9-td57q   1/1     Running     0          2m3s
postinstall-hook                      0/1     Completed   0          2m3s
preinstall-hook                       0/1     Completed   0          2m25s
```

```bash
$ kubectl describe po preinstall-hook

Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sat, 06 Apr 2024 14:53:24 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.11
IPs:
  IP:  10.244.0.11
Containers:
  pre-install-container:
    Container ID:  docker://5bff00ab357bb31be03e4ac118f3a5e4625b8c88b6f3e51b9370ef8cff7c8637
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
      Started:      Sat, 06 Apr 2024 14:53:25 +0300
      Finished:     Sat, 06 Apr 2024 14:53:45 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-bkcwr (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-bkcwr:
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
  Normal  Scheduled  3m5s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     3m4s  kubelet            Container image "busybox" already present on machine
  Normal  Created    3m4s  kubelet            Created container pre-install-container
  Normal  Started    3m4s  kubelet            Started container pre-install-container
```

```bash
$ kubectl describe po postinstall-hook

Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sat, 06 Apr 2024 14:53:46 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.13
IPs:
  IP:  10.244.0.13
Containers:
  post-install-container:
    Container ID:  docker://7bada152dbb674e22304cf35a77397b569840e117ce658934728d5f9d54a6b7f
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
      Started:      Sat, 06 Apr 2024 14:53:48 +0300
      Finished:     Sat, 06 Apr 2024 14:54:03 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-7sm8l (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-7sm8l:
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
  Normal  Scheduled  3m37s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    3m36s  kubelet            Pulling image "busybox"
  Normal  Pulled     3m35s  kubelet            Successfully pulled image "busybox" in 1.644s (1.644s including waiting)
  Normal  Created    3m35s  kubelet            Created container post-install-container
  Normal  Started    3m35s  kubelet            Started container post-install-container
```

Then I added hook-delete-policy on hook-succeeded. 
So, after rerunning commands 
```bash
$ kubectl get po
NAME                                  READY   STATUS    RESTARTS   AGE
my-helm-app-python-86f7dfdcc9-ltb64   1/1     Running   0          46s
```
there are no hooks pods