# Helm

## Task 1

### Install Chart
```shell
$ helm install my-python-app -g
NAME: my-python-app
LAST DEPLOYED: Wed Apr 10 02:43:50 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get --namespace default svc -w my-python-app'
  export SERVICE_IP=$(kubectl get svc --namespace default my-python-app --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:5000
```

### Output
```shell
$ kubectl get pods,svc
NAME                                READY   STATUS    RESTARTS   AGE
pod/my-python-app-68dcfb467-wq6rt   1/1     Running   0          56s

NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/kubernetes      ClusterIP   10.96.0.1       <none>        443/TCP    3m38s
service/my-python-app   ClusterIP   10.108.119.87   <none>        5000/TCP   57s
```

## Task 2

### Outputs of step 4

```shell
$ kubectl get po
NAME                            READY   STATUS      RESTARTS   AGE
my-python-app-68dcfb467-6brnd   1/1     Running     0          90s
postinstall-hook                0/1     Completed   0          90s
preinstall-hook                 0/1     Completed   0          103s
```

```shell
$ kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 02:55:30 +0300 
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.150
IPs:
  IP:  10.244.0.150
Containers:
  pre-install-container:
    Container ID:  docker://8cfa9527e4854df191109b26e20486caf52688e7a3f00f4be91856c3b376b5cb
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:6776a33c72b3af7582a5b301e3a08186f2c21a3409f0d2b52dfddbdbe24a5b04
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 10
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 10 Apr 2024 02:55:31 +0300 
      Finished:     Wed, 10 Apr 2024 02:55:41 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-8wh9l (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-8wh9l:
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
  Normal  Scheduled  2m41s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     2m41s  kubelet            Container image "busybox" already present on machine
  Normal  Created    2m41s  kubelet            Created container pre-install-container
  Normal  Started    2m41s  kubelet            Started container pre-install-container
```

```shell
$ kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 02:55:43 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.152
IPs:
  IP:  10.244.0.152
Containers:
  post-install-container:
    Container ID:  docker://9b2c8709006ae06e24006a3c05a379492c1281064b48285527fb0f2d3a338e0f
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:6776a33c72b3af7582a5b301e3a08186f2c21a3409f0d2b52dfddbdbe24a5b04
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 10
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 10 Apr 2024 02:55:46 +0300
      Finished:     Wed, 10 Apr 2024 02:55:56 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-tsdkd (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-tsdkd:
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
  Normal  Scheduled  4m55s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    4m55s  kubelet            Pulling image "busybox"
  Normal  Pulled     4m53s  kubelet            Successfully pulled image "busybox" in 2.155s (2.155s including waiting)
  Normal  Created    4m53s  kubelet            Created container post-install-container
  Normal  Started    4m53s  kubelet            Started container post-install-container
```
