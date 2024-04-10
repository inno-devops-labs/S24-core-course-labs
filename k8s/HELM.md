# Helm readme file

## Commands' output

- command `kubectl get pods,svc`:

    ```properties
    ahmad@ahmad:~/Desktop/devops/k8s$ kubectl get pods,svc
    NAME                              READY   STATUS    RESTARTS   AGE
    pod/app-dotnet-8fcb56c59-7mjqt    1/1     Running   0          5m23s
    pod/app-dotnet-8fcb56c59-fvwzb    1/1     Running   0          5m5s
    pod/app-dotnet-8fcb56c59-xv9dk    1/1     Running   0          5m48s
    pod/app-python-56b6b6d8f5-rrnf4   1/1     Running   0          2m17s
    pod/app-python-56b6b6d8f5-vqxcv   1/1     Running   0          4m57s
    pod/app-python-56b6b6d8f5-xfk8d   1/1     Running   0          90s
    pod/web-app-6d8b87497f-wskps      1/1     Running   0          10m

    NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
    service/app-dotnet   LoadBalancer   10.108.234.159   <pending>     8080:30775/TCP   6s
    service/app-python   LoadBalancer   10.102.24.112    <pending>     5000:30630/TCP   6s
    service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          7d2h
    service/web-app      LoadBalancer   10.100.156.190   <pending>     5000:32417/TCP   10m
    ```

- command `kubectl get po`:

    ```properties
    ahmad@ahmad:~/Desktop/devops/k8s$ kubectl get po
    NAME                          READY   STATUS      RESTARTS   AGE
    app-dotnet-8fcb56c59-7mjqt    1/1     Running     0          22m
    app-dotnet-8fcb56c59-fvwzb    1/1     Running     0          22m
    app-dotnet-8fcb56c59-xv9dk    1/1     Running     0          23m
    app-python-56b6b6d8f5-rrnf4   1/1     Running     0          19m
    app-python-56b6b6d8f5-vqxcv   1/1     Running     0          22m
    app-python-56b6b6d8f5-xfk8d   1/1     Running     0          18m
    postinstall-hook              0/1     Completed   0          3m7s
    preinstall-hook               0/1     Completed   0          3m34s
    web-app-6d8b87497f-dj4j8      1/1     Running     0          3m7s
    ```

- command `kubectl describe po preinstall-hook`:

    ```properties
    ahmad@ahmad:~/Desktop/devops/k8s$ kubectl describe po preinstall-hook
    Name:             preinstall-hook
    Namespace:        default
    Priority:         0
    Service Account:  default
    Node:             minikube/192.168.49.2
    Start Time:       Wed, 10 Apr 2024 03:43:47 +0300
    Labels:           <none>
    Annotations:      helm.sh/hook: pre-install
    Status:           Succeeded
    IP:               10.244.0.62
    IPs:
    IP:  10.244.0.62
    Containers:
    pre-install-container:
        Container ID:  docker://935dad84a3a0a76d7f4505ca71564e8a1da27c2971be8637d2d4b9487f2cdba1
        Image:         busybox
        Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
        Port:          <none>
        Host Port:     <none>
        Command:
        sh
        -c
        echo pre-install hook is running && sleep 20
        State:          Terminated
        Reason:       Completed
        Exit Code:    0
        Started:      Wed, 10 Apr 2024 03:43:51 +0300
        Finished:     Wed, 10 Apr 2024 03:44:11 +0300
        Ready:          False
        Restart Count:  0
        Environment:    <none>
        Mounts:
        /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-zvwlg (ro)
    Conditions:
    Type              Status
    Initialized       True 
    Ready             False 
    ContainersReady   False 
    PodScheduled      True 
    Volumes:
    kube-api-access-zvwlg:
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
    Normal  Scheduled  5m27s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
    Normal  Pulling    5m27s  kubelet            Pulling image "busybox"
    Normal  Pulled     5m23s  kubelet            Successfully pulled image "busybox" in 4.021s (4.021s including waiting)
    Normal  Created    5m23s  kubelet            Created container pre-install-container
    Normal  Started    5m23s  kubelet            Started container pre-install-container
    ```

- command `kubectl describe po postinstall-hook`:

    ```properties
    ahmad@ahmad:~/Desktop/devops/k8s$ kubectl describe po postinstall-hook
    Name:             postinstall-hook
    Namespace:        default
    Priority:         0
    Service Account:  default
    Node:             minikube/192.168.49.2
    Start Time:       Wed, 10 Apr 2024 03:44:14 +0300
    Labels:           <none>
    Annotations:      helm.sh/hook: post-install
    Status:           Succeeded
    IP:               10.244.0.64
    IPs:
    IP:  10.244.0.64
    Containers:
    post-install-container:
        Container ID:  docker://40c9f8e59518431d42328035093c259aec601b837510f7796db64e7baec503eb
        Image:         busybox
        Image ID:      docker-pullable://busybox@sha256:c3839dd800b9eb7603340509769c43e146a74c63dca3045a8e7dc8ee07e53966
        Port:          <none>
        Host Port:     <none>
        Command:
        sh
        -c
        echo post-install hook is running && sleep 20
        State:          Terminated
        Reason:       Completed
        Exit Code:    0
        Started:      Wed, 10 Apr 2024 03:44:16 +0300
        Finished:     Wed, 10 Apr 2024 03:44:36 +0300
        Ready:          False
        Restart Count:  0
        Environment:    <none>
        Mounts:
        /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-fzzt8 (ro)
    Conditions:
    Type              Status
    Initialized       True 
    Ready             False 
    ContainersReady   False 
    PodScheduled      True 
    Volumes:
    kube-api-access-fzzt8:
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
    Normal  Scheduled  6m32s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
    Normal  Pulling    6m32s  kubelet            Pulling image "busybox"
    Normal  Pulled     6m30s  kubelet            Successfully pulled image "busybox" in 1.545s (1.545s including waiting)
    Normal  Created    6m30s  kubelet            Created container post-install-container
    Normal  Started    6m30s  kubelet            Started container post-install-container
    ```

- Delete policy

    I added `helm.sh/hook-delete-policy": hook-succeeded` to yml hooks files.

