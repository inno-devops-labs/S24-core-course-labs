# Helm

## HELM Setup and Chart Creation

1. Creating the HELM Chart Template:

```
$ helm create helm-app-python
```

2. Modifying the default repository and tag in values.yml by ```sharmatanmay617/app_python``` and ```latest```.

3. Changing ```containerPort``` to 5000.

4. Installing custom Helm Chart:

```
$ helm install helm-app-python helm-app-python/ --values helm-app-python/values.yaml
```

### Output:

```
NAME: helm-app-python
LAST DEPLOYED: Wed Apr 10 01:43:08 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get --namespace default svc -w helm-app-python'
  export SERVICE_IP=$(kubectl get svc --namespace default helm-app-python --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:5000
```

5. ```kubectl get pods,svc```

```
NAME                                 READY   STATUS      RESTARTS   AGE
pod/helm-app-python-8bd6fc65-rvhws   1/1     Running     0          10m
pod/postinstall-hook                 0/1     Completed   0          10m
pod/preinstall-hook                  0/1     Completed   0          10m

NAME                      TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/helm-app-python   LoadBalancer   10.101.5.215   <pending>     5000:30809/TCP   10m
service/kubernetes        ClusterIP      10.96.0.1      <none>        443/TCP          15m
```

## Helm Chart Hooks

(Running without onDelete Hook)

1. Linting the helm chart

```
$ helm lint helm-app-python
```

```
==> Linting helm-app-python
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

2. ```helm install --dry-run helm-hooks helm-app-python```

```
NAME: helm-hooks
LAST DEPLOYED: Wed Apr 10 02:07:44 2024
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: helm-app-python/templates/post-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
   name: postinstall-hook
   annotations:
       "helm.sh/hook": "post-install"
      #  "helm.sh/hook-delete-policy": hook-succeeded
spec:
  containers:
  - name: post-install-container
    image: busybox
    imagePullPolicy: Always
    command: ['sh', '-c', 'echo The post-install hook is running && sleep 20' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---
```


3. ```kubectl get po```

```
NAME                             READY   STATUS      RESTARTS   AGE
helm-app-python-8bd6fc65-rvhws   1/1     Running     0          107s
postinstall-hook                 0/1     Completed   0          107s
preinstall-hook                  0/1     Completed   0          2m21s
```

4. ```kubectl describe po preinstall-hook```

```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 01:43:08 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.3
IPs:
  IP:  10.244.0.3
Containers:
  pre-install-container:
    Container ID:  docker://6bed620090553939482592fa852a41e4aa8e2ea6323bb3616001bbcbc66a1f63
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
      Started:      Wed, 10 Apr 2024 01:43:19 +0300
      Finished:     Wed, 10 Apr 2024 01:43:39 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-xsglq (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-xsglq:
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
  Normal  Scheduled  2m56s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    2m54s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m46s  kubelet            Successfully pulled image "busybox" in 7.748s (7.748s including waiting)
  Normal  Created    2m45s  kubelet            Created container pre-install-container
  Normal  Started    2m45s  kubelet            Started container pre-install-container
```

5. ```kubectl describe po postinstall-hook```

```
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 01:43:42 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.5
IPs:
  IP:  10.244.0.5
Containers:
  post-install-container:
    Container ID:  docker://313a33954a7cc5f7a5489e30c2ba934e22c90d51d949aa890b84edc3597ae9cf
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
      Started:      Wed, 10 Apr 2024 01:44:15 +0300
      Finished:     Wed, 10 Apr 2024 01:44:35 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-j76p5 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-j76p5:
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
  Normal  Scheduled  2m33s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    2m30s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m1s   kubelet            Successfully pulled image "busybox" in 4.673s (29.003s including waiting)
  Normal  Created    2m     kubelet            Created container post-install-container
  Normal  Started    2m     kubelet            Started container post-install-container
```

6. ```minikube dashboard```

![MiniKube Dashboard](https://github.com/tanmaysharma2001/S24-core-course-labs/assets/78191188/d9ee33e7-a1a6-4c1b-9f55-a3bbb5b96224)
