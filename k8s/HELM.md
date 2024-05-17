# Helm

## Results

```
NAME                                    READY   STATUS    RESTARTS        AGE
pod/app-python-deploy-f857b665d-7fqv6   1/1     Running   1 (4h39m ago)   6h29m
pod/app-python-deploy-f857b665d-w6sfw   1/1     Running   1 (4h39m ago)   6h29m
pod/app-python-deploy-f857b665d-xt7r9   1/1     Running   1 (4h39m ago)   6h29m
pod/chart-app-python-9d546b454-k8hrk    1/1     Running   1 (3m17s ago)   4h18m
pod/pchart-test-6564dcd77f-rzp8k        1/1     Running   3 (3m18s ago)   4h40m
pod/tchart-test-54d8577598-d6xm2        1/1     Running   1 (4h39m ago)   4h57m

NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/app-python-service   ClusterIP   10.96.87.170     <none>        8090/TCP   6h29m
service/chart-app-python     ClusterIP   10.97.180.177    <none>        8000/TCP   4h18m
service/kubernetes           ClusterIP   10.96.0.1        <none>        443/TCP    6h58m
service/pchart-test          ClusterIP   10.108.88.18     <none>        8080/TCP   4h40m
service/tchart-test          ClusterIP   10.110.102.255   <none>        80/TCP     4h57m
```
