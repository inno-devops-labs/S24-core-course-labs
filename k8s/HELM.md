# Ouputs Helm

## Installation

```shell
$ helm install app-python  app-python/ --values app-python/values.yaml
NAME: app-python
LAST DEPLOYED: Wed Apr  10 05:37:19 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get --namespace default svc -w app-python'
  export SERVICE_IP=$(kubectl get svc --namespace default app-python --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:8000
```

## kubectl get pods,svc
```shell
$ kubectl get pods,svc
NAME                              READY   STATUS      RESTARTS   AGE
pod/app-python-65d9f44967-6x572   1/1     Running     0          73s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.107.203.154   <pending>     8000:32680/TCP   73s
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          12m
```

## kubectl get po
```shell
$ kubectl get po
NAME                          READY   STATUS      RESTARTS   AGE
app-python-65d9f44967-6x572   1/1     Running     0          105s
post-install-hook             0/1     Completed   0          105s
pre-install-hook              0/1     Completed   0          113s
```

## kubectl describe po pre-install-hook
```shell
$ kubectl describe po pre-install-hook
Name:             pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2 Wed Apr  10 05:37:19
Start Time:       Wed, 10 Apr 2024 05:45:43 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
                  helm.sh/hook-delete-policy: hook-succeeded"
Status:           Succeeded
IP:               10.244.0.153
IPs:
  IP:  10.244.0.153
Containers:
  pre-install-container:
    Container ID:  docker://424d25b514b3ab26d6c76e63b2db8859601e98786ebcbd50f782d6e0e32dfd4d
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:6776a33c72b3af7582a5b301e3a08186f2c21a3409f0d2b52dfddbdbe24a5b04
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 5
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 10 Apr 2024 05:45:44 +0300
      Finished:     Wed, 10 Apr 2024 05:45:49 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-xkjwv (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-xkjwv:
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
  Normal  Scheduled  2m33s  default-scheduler  Successfully assigned default/pre-install-hook to minikube
  Normal  Pulled     2m32s  kubelet            Container image "busybox" already present on machine
  Normal  Created    2m32s  kubelet            Created container pre-install-container
  Normal  Started    2m32s  kubelet            Started container pre-install-container
```

## kubectl describe po post-install-hook
```shell
$ kubectl describe po post-install-hook
Name:             post-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 10 Apr 2024 05:45:51 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
                  helm.sh/hook-delete-policy: hook-succeeded"
Status:           Succeeded
IP:               10.244.0.155
IPs:
  IP:  10.244.0.155
Containers:
  post-install-container:
    Container ID:  docker://f2a212cdfa2b5502bc8857212bb048eaf6ab1938c453831bffad25d6a6a4d823
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:6776a33c72b3af7582a5b301e3a08186f2c21a3409f0d2b52dfddbdbe24a5b04
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 5
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 10 Apr 2024 05:45:54 +0300
      Finished:     Wed, 10 Apr 2024 05:45:59 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-7trqh (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-7trqh:
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
  Normal  Scheduled  2m51s  default-scheduler  Successfully assigned default/post-install-hook to minikube
  Normal  Pulling    2m50s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m48s  kubelet            Successfully pulled image "busybox" in 2.088s (2.088s including waiting)
  Normal  Created    2m48s  kubelet            Created container post-install-container
  Normal  Started    2m48s  kubelet            Started container post-install-container
```