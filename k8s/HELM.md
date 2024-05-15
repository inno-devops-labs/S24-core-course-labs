# Helm


- Output of `kubectl get pods,svc` after using helm:
```
PS D:\Roukaya\Repos\DevOps\S24-core-course-labs\k8s> kubectl get pods,svc
NAME                                      READY   STATUS    RESTARTS   AGE
pod/moscow-time-765bfbbbcd-48hvj          1/1     Running   0          2m52s
pod/python-moscow-time-847bbcd9b8-xmtvd   1/1     Running   0          25h

NAME                         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python           LoadBalancer   10.111.17.172   <pending>     5000:31552/TCP   20h
service/kubernetes           ClusterIP      10.96.0.1       <none>        443/TCP          25h
service/moscow-time          ClusterIP      10.96.246.140   <none>        80/TCP           2m53s
service/python-moscow-time   LoadBalancer   10.98.31.123    localhost     5000:31675/TCP   21h
```