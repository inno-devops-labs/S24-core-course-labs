### Deploy Application

to make deployment I used command ```kubectl create deployment web-app --image=belowzero1/app_python:v1``` which gives
me following output:

```
deployment.apps/web-app created
```

### Access Application from the outside

I used this command ```kubectl expose deployment web-app --type=LoadBalancer --port=8000``` to create service resource
and make the application accessible from outside the Kubernetes virtual network.
output of the command:
```commandline
service/web-app exposed
```
### Create a Kubernetes Folder
so, it is the file with report I was required to create. Re output of the command ```kubectl get pods,svc``` is:
```commandline
NAME                           READY   STATUS    RESTARTS   AGE
pod/web-app-7d8bbccb5c-kpjt7   1/1     Running   0          28m

NAME                 TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1     <none>        443/TCP          43m
service/web-app      LoadBalancer   10.101.5.10   <pending>     8000:31444/TCP   26m
```

### Cleanup
command to remove deployments ```kubectl delete deployment web-app```. Output:
```
deployment.apps "web-app" deleted
```
Command to remove services ```kubectl delete service web-app```. Output:
```commandline
service "web-app" deleted
```
