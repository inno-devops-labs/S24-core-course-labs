# Kubernetes Deployment and Service

## Output of kubectl get pods,svc

```bash
$ kubectl get pods,svc

NAME                                         READY   STATUS    RESTARTS   AGE
pod/app-python-deployment-6cd95fdb98-qjphf   1/1     Running   0          18m

NAME                         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python-service   NodePort    10.105.75.197   <none>        8000:30501/TCP   18m
service/kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP          38m
```