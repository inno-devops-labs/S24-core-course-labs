# HELM Lab 10

## Task 1

```bash
minikube dashboard
```
![](screenshots/dashboard.png)
```bash
minikube service my-flask-app
```
![](screenshots/service.png)
```bash
kubectl get pods,svc
```
![](screenshots/kubectl.png)

## Task 2
```bash
kubectl get po
```
![](screenshots/get_po.png)
```bash
kubectl describe po preinstall-hook
```
![](screenshots/desc1.png)
```bash
kubectl describe po postinstall-hook
```
![](screenshots/desc2.png)