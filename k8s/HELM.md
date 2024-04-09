## HELM

### Task 1

```commandline
helm create app-python
```

```commandline
helm install app-python app-python
```

```commandline
NAME: app-python
LAST DEPLOYED: Tue Apr  9 16:41:35 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=app-python,app.kubernetes.io/instance=app-python" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT

```

```commandline
kubectl get pods,svc
```

```commandline
NAME                                         READY   STATUS    RESTARTS     AGE
pod/app-python-57d59698db-ntfwm              1/1     Running   0            3m29s
pod/app-python-deployment-6f7855dc84-5dw57   1/1     Running   1 (8d ago)   8d
pod/app-python-deployment-6f7855dc84-b9slb   1/1     Running   1 (8d ago)   8d
pod/app-python-deployment-6f7855dc84-qwtcz   1/1     Running   1 (8d ago)   8d

NAME                         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python           ClusterIP      10.105.4.42     <none>        8000/TCP         3m29s
service/app-python-service   LoadBalancer   10.102.166.79   <pending>     8000:32152/TCP   8d
service/kubernetes           ClusterIP      10.96.0.1       <none>        443/TCP          8d
```

### Task 2

```commandline
kubectl get po 
```

```commandline
NAME                                     READY   STATUS      RESTARTS     AGE
app-python-57d59698db-ntfwm              1/1     Running     0            3h49m
app-python-deployment-6f7855dc84-5dw57   1/1     Running     1 (8d ago)   8d
app-python-deployment-6f7855dc84-b9slb   1/1     Running     1 (8d ago)   8d
app-python-deployment-6f7855dc84-qwtcz   1/1     Running     1 (8d ago)   8d
postinstall-hook                         0/1     Completed   0            3m47s
preinstall-hook                          0/1     Completed   0            3m41s

```

```commandline
kubectl describe po preinstall-hook
```

```commandline
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 20:27:26 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
                  helm.sh/hook-delete-policy: hook-succeeded
Status:           Succeeded
IP:               10.244.0.16
IPs:
  IP:  10.244.0.16
Containers:
  pre-install-container:
    Container ID:  docker://88c514ba973b93289731fceafde10c9206c4620e185def7f0a8ea1268dd388da
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
      Started:      Tue, 09 Apr 2024 20:27:29 +0300
      Finished:     Tue, 09 Apr 2024 20:27:49 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-hx7g5 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-hx7g5:
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
  Normal  Scheduled  8m30s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    8m29s  kubelet            Pulling image "busybox"
  Normal  Pulled     8m27s  kubelet            Successfully pulled image "busybox" in 1.657s (2.009s including waiting)
  Normal  Created    8m27s  kubelet            Created container pre-install-container
  Normal  Started    8m27s  kubelet            Started container pre-install-container
```

```commandline
kubectl describe po postinstall-hook
```

```commandline
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 20:27:20 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
                  helm.sh/hook-delete-policy: hook-succeeded
Status:           Succeeded
IP:               10.244.0.15
IPs:
  IP:  10.244.0.15
Containers:
  post-install-container:
    Container ID:  docker://6a5b297c677ab5721ae42a1d1d7d0c8b776ee314b83e6e591f106a286c606eaf
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
      Started:      Tue, 09 Apr 2024 20:27:27 +0300
      Finished:     Tue, 09 Apr 2024 20:27:42 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-ljcw4 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-ljcw4:
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
  Normal  Scheduled  9m46s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    9m45s  kubelet            Pulling image "busybox"
  Normal  Pulled     9m40s  kubelet            Successfully pulled image "busybox" in 4.696s (4.696s including waiting)
  Normal  Created    9m40s  kubelet            Created container post-install-container
  Normal  Started    9m40s  kubelet            Started container post-install-container
```