### Task 1
Output of `kubectl get pods,svc`:
```bash
NAME                                 READY   STATUS    RESTARTS   AGE
pod/app-go-6d8c66f9f9-rv9bj          1/1     Running   0          6d21h
pod/app-go-6d8c66f9f9-sprgn          1/1     Running   0          6d21h
pod/app-go-6d8c66f9f9-t2mmv          1/1     Running   0          6d21h
pod/app-python-78546c949-8s72v       1/1     Running   0          6d21h
pod/app-python-78546c949-qlcxm       1/1     Running   0          6d21h
pod/app-python-78546c949-wb5qd       1/1     Running   0          6d21h
pod/my-app-python-6c69496ddb-s5wgp   1/1     Running   0          4m39s

NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-go-service       NodePort    10.97.143.208    <none>        5002:31400/TCP   6d21h
service/app-python-service   NodePort    10.108.148.201   <none>        5001:32005/TCP   6d21h
service/kubernetes           ClusterIP   10.96.0.1        <none>        443/TCP          7d
service/my-app-python        NodePort    10.106.239.230   <none>        5001:30762/TCP   4m39s
```

Task 2:
Output of `kubectl get po`:
```bash
NAME                             READY   STATUS      RESTARTS   AGE
app-go-6d8c66f9f9-rv9bj          1/1     Running     0          6d22h
app-go-6d8c66f9f9-sprgn          1/1     Running     0          6d22h
app-go-6d8c66f9f9-t2mmv          1/1     Running     0          6d22h
app-python-78546c949-8s72v       1/1     Running     0          6d22h
app-python-78546c949-qlcxm       1/1     Running     0          6d22h
app-python-78546c949-wb5qd       1/1     Running     0          6d22h
my-app-python-6c69496ddb-qfj58   1/1     Running     0          44s
postinstall-hook                 0/1     Completed   0          44s
preinstall-hook                  0/1     Completed   0          66s
```


Output of `kubectl describe po preinstall-hook`:
```bash
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 22:15:45 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.46
IPs:
  IP:  10.244.0.46
Containers:
  pre-install-container:
    Container ID:  docker://fa02e0a49514e896d030e931460cae6f8cc6938ffddbc18f1f3b5014857c0eae
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
      Started:      Tue, 09 Apr 2024 22:15:45 +0300
      Finished:     Tue, 09 Apr 2024 22:16:05 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-mppqc (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-mppqc:
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
  Normal  Scheduled  82s   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     82s   kubelet            Container image "busybox" already present on machine
  Normal  Created    82s   kubelet            Created container pre-install-container
  Normal  Started    82s   kubelet            Started container pre-install-container
```


Output of `kubectl describe po postinstall-hook`
```bash
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 22:16:07 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.48
IPs:
  IP:  10.244.0.48
Containers:
  post-install-container:
    Container ID:  docker://e9428cdc0407bacf54375ef8622cddde24a27d6edc22e878252013c7d5bc05ef
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
      Started:      Tue, 09 Apr 2024 22:16:11 +0300
      Finished:     Tue, 09 Apr 2024 22:16:26 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-jj8df (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-jj8df:
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
  Normal  Scheduled  102s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    101s  kubelet            Pulling image "busybox"
  Normal  Pulled     98s   kubelet            Successfully pulled image "busybox" in 3.057s (3.057s including waiting)
  Normal  Created    98s   kubelet            Created container post-install-container
  Normal  Started    98s   kubelet            Started container post-install-container
```