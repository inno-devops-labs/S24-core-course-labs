## Task 1

* `helm create app-python`

* `helm install app-python ./app-python/`

* `minikube service app-python`

* `kubectl get pods,svc`
    ```bash
    NAME                            READY   STATUS    RESTARTS   AGE
    pod/app-python-f9789889-8ch56   1/1     Running   0          64s

    NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
    service/app-python   LoadBalancer   10.100.87.193   <pending>     5000:32469/TCP   64s
    service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          41h
    ```

## Task 2

* `kubectl get po`
    ```bash
    NAME                        READY   STATUS      RESTARTS   AGE
    app-python-f9789889-fqzlq   1/1     Running     0          5m
    post-install-hook           0/1     Completed   0          5m
    pre-install-hook            0/1     Completed   0          5m14s
    ```

* `kubectl describe po pre-install-hook `
    ```bash
    Name:             pre-install-hook
    Namespace:        default
    Priority:         0
    Service Account:  default
    Node:             minikube/192.168.49.2
    Start Time:       Wed, 03 Apr 2024 15:55:01 +0300
    Labels:           <none>
    Annotations:      helm.sh/hook: pre-install
                    helm.sh/hook-weight: -10
    Status:           Succeeded
    IP:               10.244.0.3
    IPs:
    IP:  10.244.0.3
    Containers:
    pre-install-container:
        Container ID:  docker://f5b12240c704ba6f3ce8881cff52ad5c938b175a1f590179dd4f9b503933692a
        Image:         busybox
        Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
        Port:          <none>
        Host Port:     <none>
        Command:
        sleep
        7
        State:          Terminated
        Reason:       Completed
        Exit Code:    0
        Started:      Wed, 03 Apr 2024 15:55:06 +0300
        Finished:     Wed, 03 Apr 2024 15:55:13 +0300
        Ready:          False
        Restart Count:  0
        Environment:    <none>
        Mounts:
        /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-hrzkk (ro)
    Conditions:
    Type              Status
    Initialized       True 
    Ready             False 
    ContainersReady   False 
    PodScheduled      True 
    Volumes:
    kube-api-access-hrzkk:
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
    Normal  Scheduled  7m19s  default-scheduler  Successfully assigned default/pre-install-hook to minikube
    Normal  Pulling    7m18s  kubelet            Pulling image "busybox"
    Normal  Pulled     7m14s  kubelet            Successfully pulled image "busybox" in 4.565s (4.565s including waiting)
    Normal  Created    7m14s  kubelet            Created container pre-install-container
    Normal  Started    7m14s  kubelet            Started container pre-install-container
    ```

* `kubectl describe po post-install-hook`

    ```bash
    Name:             post-install-hook
    Namespace:        default
    Priority:         0
    Service Account:  default
    Node:             minikube/192.168.49.2
    Start Time:       Wed, 03 Apr 2024 15:55:15 +0300
    Labels:           <none>
    Annotations:      helm.sh/hook: post-install
                    helm.sh/hook-weight: 10
    Status:           Succeeded
    IP:               10.244.0.5
    IPs:
    IP:  10.244.0.5
    Containers:
    post-install-container:
        Container ID:  docker://7fc112d61286a3d8587386593fb90f6f15af19f9e53e42e3ecdedf1f695a5d79
        Image:         busybox
        Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
        Port:          <none>
        Host Port:     <none>
        Command:
        sleep
        7
        State:          Terminated
        Reason:       Completed
        Exit Code:    0
        Started:      Wed, 03 Apr 2024 15:55:29 +0300
        Finished:     Wed, 03 Apr 2024 15:55:36 +0300
        Ready:          False
        Restart Count:  0
        Environment:    <none>
        Mounts:
        /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-rgphr (ro)
    Conditions:
    Type              Status
    Initialized       True 
    Ready             False 
    ContainersReady   False 
    PodScheduled      True 
    Volumes:
    kube-api-access-rgphr:
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
    Normal  Scheduled  8m32s  default-scheduler  Successfully assigned default/post-install-hook to minikube
    Normal  Pulling    8m32s  kubelet            Pulling image "busybox"
    Normal  Pulled     8m18s  kubelet            Successfully pulled image "busybox" in 1.997s (13.374s including waiting)
    Normal  Created    8m18s  kubelet            Created container post-install-container
    Normal  Started    8m18s  kubelet            Started container post-install-container
    ```

* `kubectl get pods,svc`
    ```bash
    NAME                            READY   STATUS      RESTARTS   AGE
    pod/app-python-f9789889-fqzlq   1/1     Running     0          39m
    pod/post-install-hook           0/1     Completed   0          39m
    pod/pre-install-hook            0/1     Completed   0          39m

    NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
    service/app-python   LoadBalancer   10.104.118.154   <pending>     5000:32207/TCP   39m
    service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          46m    
    ```

*  hook delete policy implemented using 
    - `"helm.sh/hook-delete-policy": hook-succeeded`
