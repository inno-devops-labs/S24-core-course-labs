# Task 1

I installed Helm from script, changed tag and name of the repository in `values.yml` and port in `deployment.yaml`.

```
rostislav@rostislavpc:~/devops_labs/k8s$ minikube dashboard
🤔  Verifying dashboard health ...
🚀  Launching proxy ...
🤔  Verifying proxy health ...
🎉  Opening http://127.0.0.1:43015/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/ in your default browser...
👉  http://127.0.0.1:43015/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/
```

Everything seems healthy
![](/k8s/screenshots/helm1.jpg)
![](/k8s/screenshots/helm2.jpg)

```
rostislav@rostislavpc:~/devops_labs/k8s$ minikube service helm-app
|-----------|----------|-------------|--------------|
| NAMESPACE |   NAME   | TARGET PORT |     URL      |
|-----------|----------|-------------|--------------|
| default   | helm-app |             | No node port |
|-----------|----------|-------------|--------------|
😿  service default/helm-app has no node port
🏃  Starting tunnel for service helm-app.
|-----------|----------|-------------|------------------------|
| NAMESPACE |   NAME   | TARGET PORT |          URL           |
|-----------|----------|-------------|------------------------|
| default   | helm-app |             | http://127.0.0.1:41889 |
|-----------|----------|-------------|------------------------|
🎉  Opening service default/helm-app in default browser...
👉  http://127.0.0.1:41889
❗️  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
```

![](/k8s/screenshots/helm3.jpg)

```
rostislav@rostislavpc:~/devops_labs/k8s$ kubectl get pods,svc
NAME                                           READY   STATUS    RESTARTS        AGE
pod/flask-server-deployment-68959b4dfb-6r845   1/1     Running   1 (6m18s ago)   7d5h
pod/flask-server-deployment-68959b4dfb-85c8w   1/1     Running   1 (6m18s ago)   7d5h
pod/flask-server-deployment-68959b4dfb-gmpmc   1/1     Running   1 (6m18s ago)   7d5h
pod/helm-app-587f75766-n4jdg                   1/1     Running   0               3m54s

NAME                           TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/flask-server-service   LoadBalancer   10.109.75.119    <pending>     5000:30444/TCP   7d5h
service/helm-app               ClusterIP      10.106.176.101   <none>        80/TCP           3m54s
service/kubernetes             ClusterIP      10.96.0.1        <none>        443/TCP          7d5h
```

# Task 2

```
rostislav@rostislavpc:~/devops_labs/k8s$ kubectl get po
NAME                                       READY   STATUS      RESTARTS      AGE
flask-server-deployment-68959b4dfb-6r845   1/1     Running     1 (34m ago)   7d5h
flask-server-deployment-68959b4dfb-85c8w   1/1     Running     1 (34m ago)   7d5h
flask-server-deployment-68959b4dfb-gmpmc   1/1     Running     1 (34m ago)   7d5h
helm-app-587f75766-n4jdg                   1/1     Running     0             32m
helm-hooks-helm-app-866d64484c-f2zv4       1/1     Running     0             3m57s
postinstall-hook                           0/1     Completed   0             3m57s
pre-install-hook                           0/1     Completed   0             4m20s
```

```
rostislav@rostislavpc:~/devops_labs/k8s$ kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 19:22:19 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.16
IPs:
  IP:  10.244.0.16
Containers:
  post-install-container:
    Container ID:  docker://affb2a10805e58a637426f4fb9b859752881f0f83a1660da83e368c7eb4dbfaf
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
      Started:      Tue, 09 Apr 2024 19:22:22 +0300
      Finished:     Tue, 09 Apr 2024 19:22:37 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-fn8mt (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-fn8mt:
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
  Normal  Scheduled  6m22s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    6m22s  kubelet            Pulling image "busybox"
  Normal  Pulled     6m20s  kubelet            Successfully pulled image "busybox" in 1.936s (1.936s including waiting)
  Normal  Created    6m20s  kubelet            Created container post-install-container
  Normal  Started    6m20s  kubelet            Started container post-install-container
```

```
rostislav@rostislavpc:~/devops_labs/k8s$ kubectl describe po pre-install-hook
Name:             pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 09 Apr 2024 19:21:56 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.14
IPs:
  IP:  10.244.0.14
Containers:
  pre-install-container:
    Container ID:  docker://e3e977dfc9e834578c9e18232ebd1f2e9c13b2dc0f73f2eabb485b5837121d28
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 15
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 09 Apr 2024 19:22:02 +0300
      Finished:     Tue, 09 Apr 2024 19:22:17 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-zp9d2 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-zp9d2:
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
  Normal  Scheduled  7m21s  default-scheduler  Successfully assigned default/pre-install-hook to minikube
  Normal  Pulling    7m21s  kubelet            Pulling image "busybox"
  Normal  Pulled     7m15s  kubelet            Successfully pulled image "busybox" in 5.621s (5.621s including waiting)
  Normal  Created    7m15s  kubelet            Created container pre-install-container
  Normal  Started    7m15s  kubelet            Started container pre-install-container
```