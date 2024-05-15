# Kubernetes

## Command Outputs

- Manually creating the deployment and service:
```
PS D:\Roukaya\Repos\DevOps\S24-core-course-labs> kubectl create deployment python-moscow-time --image=roukayazaki/roukaya
deployment.apps/python-moscow-time created
PS D:\Roukaya\Repos\DevOps\S24-core-course-labs> kubectl get deployments
NAME                 READY   UP-TO-DATE   AVAILABLE   AGE
python-moscow-time   1/1     1            1           3h48m
PS D:\Roukaya\Repos\DevOps\S24-core-course-labs> kubectl get pods
NAME                                  READY   STATUS    RESTARTS   AGE
python-moscow-time-847bbcd9b8-xmtvd   1/1     Running   0          3h48m
PS D:\Roukaya\Repos\DevOps\S24-core-course-labs> kubectl expose deployment python-moscow-time --type=LoadBalancer --port=5000
service/python-moscow-time exposed
```

- Output of `kubectl get pods,svc` after manually creating a deployment and a service:
```
PS D:\Roukaya\Repos\DevOps\S24-core-course-labs> kubectl get pods,svc
NAME                                      READY   STATUS    RESTARTS   AGE
pod/python-moscow-time-847bbcd9b8-xmtvd   1/1     Running   0          3h51m

NAME                         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes           ClusterIP      10.96.0.1      <none>        443/TCP          3h59m
service/python-moscow-time   LoadBalancer   10.98.31.123   localhost     5000:31675/TCP   24s
```

- After using configuration files and creating 3 replicas:
```
PS D:\Roukaya\Repos\DevOps\S24-core-course-labs> kubectl get pods,svc
NAME                                      READY   STATUS    RESTARTS   AGE
pod/moscow-time-55b7bdbccd-gqt96          1/1     Running   0          2m13s
pod/moscow-time-55b7bdbccd-jrdc9          1/1     Running   0          2m13s
pod/moscow-time-55b7bdbccd-vgv2r          1/1     Running   0          2m13s
pod/python-moscow-time-847bbcd9b8-xmtvd   1/1     Running   0          4h17m

NAME                         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python           LoadBalancer   10.111.17.172   <pending>     5000:31552/TCP   3s
service/kubernetes           ClusterIP      10.96.0.1       <none>        443/TCP          4h25m
service/python-moscow-time   LoadBalancer   10.98.31.123    localhost     5000:31675/TCP   26m

```
