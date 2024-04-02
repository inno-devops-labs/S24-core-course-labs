```bash
➜  kubectl get pods,svc
NAME                                  READY   STATUS    RESTARTS   AGE
pod/app-python-node-f797d4bc5-xm77w   1/1     Running   0          6m

NAME                      TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/app-python-node   LoadBalancer   10.108.25.45   <pending>     8080:32434/TCP   74s
service/kubernetes        ClusterIP      10.96.0.1      <none>        443/TCP          8m7s
```