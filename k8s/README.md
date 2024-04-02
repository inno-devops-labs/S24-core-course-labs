# Task 1.3
## Command:
To create deployment resource
```bash
kubectl create deployment app-node --image=glebuben/dev-ops-labs
```
# Task 1.4
## Commands:
To start service that exposes ports for application.
```bash
kubectl expose deployment app-node --type=LoadBalancer --port=5000
```
To get the app response
```bash
minikube service app-node
```
# Task 1.5
## Command:
```bash
kubectl get pods,svc
```
## Output:
```bash
NAME                            READY   STATUS    RESTARTS   AGE
pod/app-node-7bd755cb98-lrg8s   1/1     Running   0          10m

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-node     LoadBalancer   10.108.161.235   <pending>     5000:30148/TCP   5m47s
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          42m
```
# Task 1.6
## Commands:
To delete deployment resource
```bash
kubectl delete deployment app-node
```
To delete service
```bash
kubectl delete deployment app-node
```