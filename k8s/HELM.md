### Install Helm Chart
I used command ``` helm install web-app web-app``` to install my custom chart, this command gives me that output:
```
NAME: web-app
LAST DEPLOYED: Wed May 15 01:09:01 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get --namespace default svc -w web-app'
  export SERVICE_IP=$(kubectl get svc --namespace default web-app --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:5000
```

After that I checked minikube dashboard to ensure that all workloads are working:
![dashboard_screenshot_1](https://github.com/MinusOne-1/DevOpsUI-s24-labs/blob/lab10/k8s/pictures/minikube_dashboard_workload1.jpg)
![dashboard_screenshot_2](https://github.com/MinusOne-1/DevOpsUI-s24-labs/blob/lab10/k8s/pictures/minikube_dashboard_workload2.jpg)

### Output of the ```kubectl get pods,svc ``` command then the app is deployed
```commandline
NAME                           READY   STATUS    RESTARTS   AGE
pod/web-app-7cd9f978f7-pv24p   1/1     Running   0          3h5m

NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          10h
service/web-app      LoadBalancer   10.110.224.3   <pending>     5000:30632/TCP   3h5m
```
