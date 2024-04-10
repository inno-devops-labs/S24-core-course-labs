# HELM

## Installation

First, we need to install helm:

```bash
root@SSD002:~/DevOps-S24/k8s$ curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
root@SSD002:~/DevOps-S24/k8s$ chmod 700 get_helm.sh
root@SSD002:~/DevOps-S24/k8s$ ./get_helm.sh
root@SSD002:~/DevOps-S24/k8s$ helm version
version.BuildInfo{Version:"v3.14.3", GitCommit:"f03cc04caaa8f6d7c3e67cf918929150cf6f3f12", GitTreeState:"clean", GoVersion:"go1.21.7"}
```

Next, create charts with `helm create`:

```bash
root@SSD002:~/DevOps-S24/k8s$ helm create py-chart
Creating py-chart
root@SSD002:~/DevOps-S24/k8s$ helm create go-chart
Creating go-chart

```

Change the necessary values in `values.yaml`:

```yaml
image:
  repository: ramprin/devops_py
  pullPolicy: IfNotPresent
  tag: "latest"
service:
  type: NodePort
  port: 8080
```

Same for go:

```yaml
image:
  repository: ramprin/devops_go
  pullPolicy: IfNotPresent
  tag: "latest"
service:
  type: NodePort
  port: 8080
```

Lint and run:

```bash
root@SSD002:~/DevOps-S24/k8s$ helm lint py-chart/
==> Linting py-chart/
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

```bash
root@SSD002:~/DevOps-S24/k8s$ helm lint go-chart/
==> Linting go-chart/
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

```bash
root@SSD002:~/DevOps-S24/k8s$ helm install py-helm ./py-chart/
NAME: py-helm
LAST DEPLOYED: Wed Apr 10 02:20:53 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services py-helm-py-chart)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
```

```bash
root@SSD002:~/DevOps-S24/k8s$ helm install go-helm ./go-chart/
NAME: go-helm
LAST DEPLOYED: Wed Apr 10 02:25:32 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services py-helm-py-chart)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
```

Results:

```bash
root@SSD002:~/DevOps-S24/k8s$ minikube service --all 
|-----------|------------------|-------------|---------------------------|
| NAMESPACE |       NAME       | TARGET PORT |            URL            |
|-----------|------------------|-------------|---------------------------|
| default   | go-helm-go-chart | http/8080   | http://192.168.49.2:31836 |
|-----------|------------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|------------------|-------------|---------------------------|
| NAMESPACE |       NAME       | TARGET PORT |            URL            |
|-----------|------------------|-------------|---------------------------|
| default   | py-helm-py-chart | http/8080   | http://192.168.49.2:32146 |
|-----------|------------------|-------------|---------------------------|
🎉  Opening service default/go-helm-go-chart in default browser...
👉  http://192.168.49.2:31836
🎉  Opening service default/py-helm-py-chart in default browser...
👉  http://192.168.49.2:32146
```
