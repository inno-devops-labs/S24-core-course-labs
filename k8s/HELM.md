# HELM

---

## Commands

> Command
>
> ```shell
> kubectl get pods
> ```
> Output
> ```shell
> NAME                                       READY   STATUS    RESTARTS   AGE
> chart-1712704918-my-apps-fcfcb845b-9zwv2   1/1     Running   0          87s
> ```

> Command
>
> ```shell
> kubectl get svc
> ```
>
> Output
>
> ```shell
> NAME                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
> chart-1712704918-my-apps   ClusterIP   10.106.116.179   <none>        80/TCP    3m36s
> kubernetes                 ClusterIP   10.96.0.1        <none>        443/TCP   14m
> ```

> Command
>
> ```shell
> kubectl get po
> ```
>
> Output
>
> ```shell
> NAME                                  READY   STATUS      RESTARTS   AGE
> helm-hooks-my-apps-6c94c46bb4-xswkv   1/1     Running     0          2m15s
> postinstall-hook                      0/1     Completed   0          2m15s
> preinstall-hook                       0/1     Completed   0          2m38s
> ```

> Command
>
> ```shell
> kubectl describe po preinstall-hook
> ```
>
> Output
>
> ```shell
> Name:             preinstall-hook
> Namespace:        default
> Priority:         0
> Service Account:  default
> Node:             minikube/192.168.59.101
> Start Time:       Wed, 10 Apr 2024 07:27:41 +0300
> Labels:           <none>
> Annotations:      helm.sh/hook: pre-install
> Status:           Succeeded
> IP:               10.244.0.11
> IPs:
>   IP:  10.244.0.11
> Containers:
>   pre-install-container:
>     Container ID:  docker://da2e72d4f49e24e2545b2bade010472a90c4cb699c6d82f7dde12aa2d789b58c
>     Image:         busybox
>     Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
>     Port:          <none>
>     Host Port:     <none>
>     Command:
>       sh
>       -c
>       echo The pre-install hook is running && sleep 20
>     State:          Terminated
>       Reason:       Completed
>       Exit Code:    0
>       Started:      Wed, 10 Apr 2024 07:27:42 +0300
>       Finished:     Wed, 10 Apr 2024 07:28:02 +0300
>     Ready:          False
>     Restart Count:  0
>     Environment:    <none>
>     Mounts:
>       /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-pztr4 (ro)
> Conditions:
>   Type              Status
>   Initialized       True
>   Ready             False
>   ContainersReady   False
>   PodScheduled      True
> Volumes:
>   kube-api-access-pztr4:
>     Type:                    Projected (a volume that contains injected data from multiple sources)
>     TokenExpirationSeconds:  3607
>     ConfigMapName:           kube-root-ca.crt
>     ConfigMapOptional:       <nil>
>    DownwardAPI:             true
> QoS Class:                   BestEffort
> Node-Selectors:              <none>
> Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
>                              node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
> Events:
>   Type    Reason     Age    From               Message
>   ----    ------     ----   ----               -------
>   Normal  Scheduled  7m17s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
>   Normal  Pulled     7m16s  kubelet            Container image "busybox" already present on machine
>   Normal  Created    7m16s  kubelet            Created container pre-install-container
>   Normal  Started    7m16s  kubelet            Started container pre-install-container
> ```

> Command
>
> ```shell
> kubectl describe po postinstall-hook
> ```
> 
> Output
> 
> ```shell
> Name:             postinstall-hook
> Namespace:        default
> Priority:         0
> Service Account:  default
> Node:             minikube/192.168.59.101
> Start Time:       Wed, 10 Apr 2024 07:28:04 +0300
> Labels:           <none>
> Annotations:      helm.sh/hook: post-install
> Status:           Succeeded
> IP:               10.244.0.13
> IPs:
>   IP:  10.244.0.13
> Containers:
>   post-install-container:
>     Container ID:  docker://804486a07668607465a060c0bf9cf168152b911aae904a4bf7eacbaaa3b8add7
>     Image:         busybox
>     Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
>     Port:          <none>
>     Host Port:     <none>
>     Command:
>       sh
>       -c
>       echo The post-install hook is running && sleep 15
>     State:          Terminated
>       Reason:       Completed
>       Exit Code:    0
>       Started:      Wed, 10 Apr 2024 07:28:06 +0300
>       Finished:     Wed, 10 Apr 2024 07:28:21 +0300
>     Ready:          False
>     Restart Count:  0
>     Environment:    <none>
>     Mounts:
>       /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-xqrql (ro)
> Conditions:
>   Type              Status
>   Initialized       True
>   Ready             False
>   ContainersReady   False
>   PodScheduled      True
> Volumes:
>   kube-api-access-xqrql:
>     Type:                    Projected (a volume that contains injected data from multiple sources)
>     TokenExpirationSeconds:  3607
>     ConfigMapName:           kube-root-ca.crt
>     ConfigMapOptional:       <nil>
>     DownwardAPI:             true
> QoS Class:                   BestEffort
> Node-Selectors:              <none>
> Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
>                              node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
> Events:
>   Type    Reason     Age   From               Message
>   ----    ------     ----  ----               -------
>   Normal  Scheduled  10m   default-scheduler  Successfully assigned default/postinstall-hook to minikube
>   Normal  Pulling    10m   kubelet            Pulling image "busybox"
>   Normal  Pulled     10m   kubelet            Successfully pulled image "busybox" in 1.571s (1.571s including waiting)
>   Normal  Created    10m   kubelet            Created container post-install-container
>   Normal  Started    10m   kubelet            Started container post-install-container
> ```