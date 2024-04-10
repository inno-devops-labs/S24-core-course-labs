# Helm

## Helm Setup

1. Install Helm:
   ```shell
   helm repo add stable https://charts.helm.sh/stable
   helm repo update
   ```

2. Create Your Own Helm Chart:
   ```shell
   helm create helm_python_app
   ```

## Install Helm Chart

1. Install the Helm chart using the following command:
```shell
helm install python ./helm_python_app
```

2. Lint the Helm chart to ensure that the syntax is correct:
```shell
helm lint ./helm_python_app
```

3. Install the Helm chart using the following command:
```shell
helm install python ./helm_python_app
```

4. Verify that jobs are created:
```shell
kubectl get po
```


## Outputs of get pod, svc

% kubectl get pods, svc 
NAME                                                READY   STATUS      RESTARTS    AGE
pod/moscow-tz-54ddff5b74-h7tw7                      1/1     Running     1 (72m ago) 104m
pod/moscow-tz-54ddff5b74-lkbmg                      1/1     Running     1 (72m ago) 104m
pod/moscow-tz-js-84f7664dcc-qlcll                   1/1     Running     1 (72m ago) 104m
pod/moscow-tz-js-84f7664dcc-rg4bf                   1/1     Running     1 (72m ago) 104m
pod/python-helm-app-python-77c647b885-6mm4p         1/1     Running     1 (72m ago) 75m

NAME                                       TYPE             CLUSTER-IP      EXTERNAL-IP     PORT(S)             AGE
service/kubernetes                         ClusterIP        10.96.0.1       <none>          443/TCP             105m
service/moscow-tz-service                  LoadBalancer     10.109.170.249  127.0.0.1       5001:30823/TCP      104m
service/python-helm-app-python             LoadBalancer     10.100.151.65   127.0.0.1       5001:30951/TCP      75m
service/r2-helm-app-python                 ClusterIP        10.108.119.56   <none>          5001/TCP            98m
