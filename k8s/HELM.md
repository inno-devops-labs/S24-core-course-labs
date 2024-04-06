# Helm

## Chart for the Python application

1. Install helm chart

    ```bash
    $ helm install app-python app-python
    NAME: app-python
    LAST DEPLOYED: Sat Apr  6 13:04:51 2024
    NAMESPACE: default
    STATUS: deployed
    REVISION: 1
    NOTES:
    1. Get the application URL by running these commands:
    export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services app-python)
    export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
    echo http://$NODE_IP:$NODE_PORT
    ```

1. Access the Minikube dashboard to ensure that all services are healthy

    ![Workloads page in the Minikube
    dashboard](assets/python-app-minikube-dashboard.png)

1. Access the application via `curl`

    ```bash
    $ minikube service app-python
    |-----------|------------|-------------|---------------------------|
    | NAMESPACE |    NAME    | TARGET PORT |            URL            |
    |-----------|------------|-------------|---------------------------|
    | default   | app-python | http/80     | http://192.168.49.2:30953 |
    |-----------|------------|-------------|---------------------------|
    🎉  Opening service default/app-python in default browser...
    👉  http://192.168.49.2:30953

    $ curl http://192.168.49.2:30953
    {"current_time":"2024-04-06 13:06:42"}
    ```

1. Verify the deployment

    ```bash
    $ kubectl get pods,svc
    NAME                              READY   STATUS    RESTARTS   AGE
    pod/app-python-584d7c68b9-6cpdq   1/1     Running   0          7m22s

    NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
    service/app-python   NodePort    10.108.38.252   <none>        80:30953/TCP   7m22s
    service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP        36m    
    ```

## Helm Chart Hooks

1. Lint the Helm chart

    ```bash
    $ helm lint app-python/
    ==> Linting app-python/

    1 chart(s) linted, 0 chart(s) failed
    ```

1. Perform dry-run of the Helm chart (output is truncated)

    ```bash
    $ helm install --dry-run helm-hooks app-python
    NAME: helm-hooks
    LAST DEPLOYED: Sat Apr  6 13:53:44 2024
    NAMESPACE: default
    STATUS: pending-install
    REVISION: 1
    HOOKS:
    ---
    # Source: app-python/templates/post-install-hook.yaml
    apiVersion: v1
    kind: Pod
    metadata:
    name: postinstall-hook
    annotations:
        "helm.sh/hook": "post-install"
    ...
    ```

1. Verify the Helm chart hooks (without hook delete policy)

    ```bash
    $ kubectl get po
    NAME                                     READY   STATUS      RESTARTS   AGE
    helm-hooks-app-python-544c64f4d4-cvdkk   1/1     Running     0          5m36s
    postinstall-hook                         0/1     Completed   0          5m36s
    preinstall-hook                          0/1     Completed   0          7m3s
    
    $ kubectl describe po preinstall-hook
    Name:             preinstall-hook
    Namespace:        default
    Priority:         0
    Service Account:  default
    Node:             minikube/192.168.49.2
    Start Time:       Sat, 06 Apr 2024 13:56:28 +0300
    Labels:           <none>
    Annotations:      helm.sh/hook: pre-install
    Status:           Succeeded
    IP:               10.244.0.8
    IPs:
    IP:  10.244.0.8
    Containers:
    pre-install-container:
        Container ID:  docker://2b424f17aa781d7b19be654d6048b9fb5c772f26e074c98a52e2bc75f42a980e
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
        Started:      Sat, 06 Apr 2024 13:57:33 +0300
        Finished:     Sat, 06 Apr 2024 13:57:53 +0300
        Ready:          False
        Restart Count:  0
        Environment:    <none>
        Mounts:
        /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-5z5qm (ro)
    Conditions:
    Type              Status
    Initialized       True 
    Ready             False 
    ContainersReady   False 
    PodScheduled      True 
    Volumes:
    kube-api-access-5z5qm:
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
    Type     Reason     Age                   From               Message
    ----     ------     ----                  ----               -------
    Normal   Scheduled  7m10s                 default-scheduler  Successfully assigned default/preinstall-hook to minikube
    Warning  Failed     6m53s                 kubelet            Failed to pull image "busybox": Error response from daemon: Head "https://registry-1.docker.io/v2/library/busybox/manifests/latest": Get "https://auth.docker.io/token?scope=repository%3Alibrary%2Fbusybox%3Apull&service=registry.docker.io": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
    Warning  Failed     6m53s                 kubelet            Error: ErrImagePull
    Normal   BackOff    6m52s                 kubelet            Back-off pulling image "busybox"
    Warning  Failed     6m52s                 kubelet            Error: ImagePullBackOff
    Normal   Pulling    6m40s (x2 over 7m9s)  kubelet            Pulling image "busybox"
    Normal   Pulled     6m5s                  kubelet            Successfully pulled image "busybox" in 35.012s (35.012s including waiting)
    Normal   Created    6m5s                  kubelet            Created container pre-install-container
    Normal   Started    6m5s                  kubelet            Started container pre-install-container
    
    $ kubectl describe po postinstall-hook
    Name:             postinstall-hook
    Namespace:        default
    Priority:         0
    Service Account:  default
    Node:             minikube/192.168.49.2
    Start Time:       Sat, 06 Apr 2024 13:57:55 +0300
    Labels:           <none>
    Annotations:      helm.sh/hook: post-install
    Status:           Succeeded
    IP:               10.244.0.10
    IPs:
    IP:  10.244.0.10
    Containers:
    post-install-container:
        Container ID:  docker://6e652f38e7bdbad7712f20e0bf9c6d7160f53b44cebfbf5257cbc3f50b6a8c1e
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
        Started:      Sat, 06 Apr 2024 13:58:11 +0300
        Finished:     Sat, 06 Apr 2024 13:58:26 +0300
        Ready:          False
        Restart Count:  0
        Environment:    <none>
        Mounts:
        /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-fcnkf (ro)
    Conditions:
    Type              Status
    Initialized       True 
    Ready             False 
    ContainersReady   False 
    PodScheduled      True 
    Volumes:
    kube-api-access-fcnkf:
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
    Normal  Scheduled  5m47s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
    Normal  Pulling    5m46s  kubelet            Pulling image "busybox"
    Normal  Pulled     5m31s  kubelet            Successfully pulled image "busybox" in 14.47s (14.47s including waiting)
    Normal  Created    5m31s  kubelet            Created container post-install-container
    Normal  Started    5m31s  kubelet            Started container post-install-container
    ```

1. Verify that only the application pod in running after enabling the hook
   delete policy

    ```bash
    $ kubectl get pods,svc
    NAME                                                       READY   STATUS    RESTARTS   AGE
    pod/hooks-with-delete-policy-app-python-5f8d6745bc-9pv4b   1/1     Running   0          15s
    ```

    P.S: As the hook delete policy is enabled, the pre-install and post-install
    pods are deleted after they are successfully executed.

## Chart for the Rust application

For this chart, I followed the same procees as for the chart for Python
application.

## Helm Library Chart

I've manually created a library chart following the structure from the provided
tutorial. The library chart is located in the `library-chart` directory.

1. Update dependencies

    ```bash
    $ helm dependency update app-python
    Saving 1 charts
    Deleting outdated charts

    $ helm dependency update app-rust
    Saving 1 charts
    Deleting outdated charts
    ```

1. Install the Python application using the library chart

    ```bash
    $ helm install app-python-library app-python
    NAME: app-python-library
    LAST DEPLOYED: Sat Apr  6 15:33:49 2024
    NAMESPACE: default
    STATUS: deployed
    REVISION: 1
    NOTES:
    1. Get the application URL by running these commands:
    export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services app-python-library)
    export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
    echo http://$NODE_IP:$NODE_PORT
    ```

1. Install the Rust application using the library chart

    ```bash
    $ helm install app-rust-library app-rust
    NAME: app-rust-library
    LAST DEPLOYED: Sat Apr  6 15:36:18 2024
    NAMESPACE: default
    STATUS: deployed
    REVISION: 1
    NOTES:
    1. Get the application URL by running these commands:
    export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services app-rust-library)
    export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
    echo http://$NODE_IP:$NODE_PORT
    ```

1. Verify the deployment

    ```bash
    $ kubectl get pods,svc
    NAME                                      READY   STATUS    RESTARTS   AGE
    pod/app-python-library-5b89b455cc-zzqz2   1/1     Running   0          3m16s
    pod/app-rust-library-595cd56945-l7pw6     1/1     Running   0          71s

    NAME                         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
    service/app-python-library   NodePort    10.106.171.50   <none>        80:31536/TCP   3m16s
    service/app-rust-library     NodePort    10.101.12.73    <none>        80:30400/TCP   71s
    service/kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP
    3h2m
    ```
