# Introduction to Helm

## Task 1
Output of `kubectl get pods,svc` command:
```commandline
yegor@yegor:~/devops/S24-Devops-core-course-labs/k8s$ kubectl get pods,svc
NAME                                         READY   STATUS    RESTARTS   AGE
pod/app-python-1711832250-7479c799cb-8r7mr   1/1     Running   0          5m

NAME                            TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python-1711832250   LoadBalancer   10.96.249.232   <pending>     8080:30411/TCP   5m
service/kubernetes              ClusterIP      10.96.0.1       <none>        443/TCP          4d8h
```

## Task 2

1. Output of `kubectl get po` command:
```commandline
yegor@yegor:~/devops/S24-Devops-core-course-labs/k8s$ kubectl get po
NAME                                     READY   STATUS      RESTARTS   AGE
app-python-1711835398-679cdb8444-qrw6c   1/1     Running     0          42s
post-install-hook                        0/1     Completed   0          42s
pre-install-hook                         0/1     Completed   0          50s
```

2. Output of `kubectl describe po pre-install-hook` command:
```commandline
yegor@yegor:~/devops/S24-Devops-core-course-labs/k8s$ kubectl describe po pre-install-hook
Name:             pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 31 Mar 2024 00:49:59 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.35
IPs:
  IP:  10.244.0.35
Containers:
  pre-install-container:
    Container ID:  docker://3574951d3c15644a19f37faee4cdfdf8311083e0d10b31a2dfe3968042413106
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 5
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 31 Mar 2024 00:50:00 +0300
      Finished:     Sun, 31 Mar 2024 00:50:05 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-wvd8p (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-wvd8p:
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
  Normal  Scheduled  81s   default-scheduler  Successfully assigned default/pre-install-hook to minikube
  Normal  Pulled     80s   kubelet            Container image "busybox" already present on machine
  Normal  Created    80s   kubelet            Created container pre-install-container
  Normal  Started    80s   kubelet            Started container pre-install-container
```

3. Output of `kubectl describe po post-install-hook` command:
```commandline
yegor@yegor:~/devops/S24-Devops-core-course-labs/k8s$ kubectl describe po post-install-hook
Name:             post-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 31 Mar 2024 00:50:07 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.37
IPs:
  IP:  10.244.0.37
Containers:
  post-install-container:
    Container ID:  docker://7ad40b5abf5045b55ba711a3f87717f49fefcf2e2c63ce5fedc3226d240e619d
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
      Started:      Sun, 31 Mar 2024 00:50:08 +0300
      Finished:     Sun, 31 Mar 2024 00:50:18 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-bnjq7 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-bnjq7:
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
  Normal  Scheduled  2m33s  default-scheduler  Successfully assigned default/post-install-hook to minikube
  Normal  Pulled     2m33s  kubelet            Container image "busybox" already present on machine
  Normal  Created    2m33s  kubelet            Created container post-install-container
  Normal  Started    2m33s  kubelet            Started container post-install-container
```

4. Output of `kubectl get pods,svc` command:
```commandline
yegor@yegor:~/devops/S24-Devops-core-course-labs/k8s$ kubectl get pods,svc
NAME                                         READY   STATUS      RESTARTS   AGE
pod/app-python-1711835398-679cdb8444-qrw6c   1/1     Running     0          3m31s
pod/post-install-hook                        0/1     Completed   0          3m31s
pod/pre-install-hook                         0/1     Completed   0          3m39s

NAME                            TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python-1711835398   LoadBalancer   10.110.173.207   <pending>     8080:31696/TCP   3m31s
service/kubernetes              ClusterIP      10.96.0.1        <none>        443/TCP          4d8h
```

Delete policy is implemented, however, I commented it before showing outputs since hooks delete after the installation. Now delete policy is uncommented.