# Kubernetes setup

### Task 1 - Output of kubectl get pods,svc
```commandline
(venv) nikitazorin@MacBook-Pro-Nikita S24-core-course-labs % kubectl get pods,svc                                                                   
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-c8c56d777-z8n6w   1/1     Running   0          31s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.108.203.72   <pending>     5000:30703/TCP   15s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          7m55s
```

### Task 2 - Screenshots for manifests

![1](screenshots/1.png)
![2](screenshots/2.png)
