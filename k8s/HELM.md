# HELM

## Setup and Chart creation

```bash
$ kubectl get svc,pods
NAME                         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/devops-lab-web-app   ClusterIP   10.105.49.104   <none>        5000/TCP         57m
service/kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP          10d
service/web-app-service      NodePort    10.99.1.159     <none>        8080:30007/TCP   9d

NAME                                      READY   STATUS    RESTARTS      AGE
pod/devops-lab-web-app-7d94cf6d98-mb2dm   1/1     Running   0             57m
pod/web-app-deployment-856645cfdd-7ccdb   1/1     Running   1 (60m ago)   9d
```

## Setup HELM Hooks

### Without delete policy

```bash
$ kubectl get po
NAME                                             READY   STATUS      RESTARTS   AGE
helm-hooks-devops-lab-web-app-5db4796cdf-b459x   1/1     Running     0          2m4s
postinstall-hook                                 0/1     Completed   0          2m4s
preinstall-hook                                  0/1     Completed   0          2m28s
web-app-deployment-856645cfdd-sj7fl              1/1     Running     0          23m

$ kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 16:56:09 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.28
IPs:
  IP:  10.244.0.28
Containers:
  pre-install-container:
    Container ID:  docker://40e255ad63e3b4c0eb12b74d1420cdbaed9965ff651814b74823e6675986aa73
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
      Started:      Tue, 09 Apr 2024 16:56:10 +0300
      Finished:     Tue, 09 Apr 2024 16:56:30 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-r79ts (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-r79ts:
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
  Normal  Scheduled  3m8s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     3m7s  kubelet            Container image "busybox" already present on machine
  Normal  Created    3m7s  kubelet            Created container pre-install-container
  Normal  Started    3m7s  kubelet            Started container pre-install-container
$ kubectl describe po postinstall-hoo
k
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 16:56:33 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.30
IPs:
  IP:  10.244.0.30
Containers:
  post-install-container:
    Container ID:  docker://22769221a5d0a822b28d19474159f070ca8467e1607b46b3fecaaa9f604da900
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
      Started:      Tue, 09 Apr 2024 16:56:36 +0300
      Finished:     Tue, 09 Apr 2024 16:56:51 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-hcrs8 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-hcrs8:
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
  Normal  Scheduled  2m49s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    2m48s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m46s  kubelet            Successfully pulled image "busybox" in 1.884s (1.884s including waiting)
  Normal  Created    2m46s  kubelet            Created container post-install-container
  Normal  Started    2m46s  kubelet            Started container post-install-container
```

### Without delete policy

```bash
$ helm install helm-hooks devops-lab-
web-app
NAME: helm-hooks
LAST DEPLOYED: Tue Apr  9 17:02:01 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=devops-lab-web-app,app.kubernetes.io/instance=helm-hooks" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
$ kubectl get po
NAME                                             READY   STATUS    RESTARTS   AGE
helm-hooks-devops-lab-web-app-5db4796cdf-xw96d   1/1     Running   0          24s
web-app-deployment-856645cfdd-sj7fl              1/1     Running   0          27m
$ kubectl get svc,pods
NAME                                    TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
service/helm-hooks-devops-lab-web-app   ClusterIP   10.97.8.152   <none>        5000/TCP         87s
service/kubernetes                      ClusterIP   10.96.0.1     <none>        443/TCP          10d
service/web-app-service                 NodePort    10.99.1.159   <none>        8080:30007/TCP   9d

NAME                                                 READY   STATUS    RESTARTS   AGE
pod/helm-hooks-devops-lab-web-app-5db4796cdf-xw96d   1/1     Running   0          87s
pod/web-app-deployment-856645cfdd-sj7fl              1/1     Running   0          28m
```