# Kubernetes

## Manual setup

```
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/web-app-py-64bf47b878-9gb7c   1/1     Running   0          62s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP        22m
service/web-app-py   LoadBalancer   10.109.167.161   <pending>     80:30520/TCP   39s
```

## Manifest-based setup

```
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/web-app-py-54bf57f5d4-g8ktf   1/1     Running   0          3m23s
pod/web-app-py-54bf57f5d4-k8ngh   1/1     Running   0          3m23s
pod/web-app-py-54bf57f5d4-p4d6p   1/1     Running   0          3m23s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          4m43s
service/web-app-py   LoadBalancer   10.105.228.85   <pending>     5000:31951/TCP   3m23s
$ minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | web-app-py |        5000 | http://192.168.49.2:31951 |
|-----------|------------|-------------|---------------------------|
🎉  Opening service default/web-app-py in default browser...
Opening in existing browser session.
$
```

## Ingress

```
$ curl --resolve "kolay.ne:80:$( minikube ip )" --verbose http://kolay.ne/ ; echo
* Added kolay.ne:80:192.168.49.2 to DNS cache
* Hostname kolay.ne was found in DNS cache
*   Trying 192.168.49.2:80...
* Connected to kolay.ne (192.168.49.2) port 80
> GET / HTTP/1.1
> Host: kolay.ne
> User-Agent: curl/8.7.1
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 404 Not Found
< Date: Fri, 29 Mar 2024 13:58:46 GMT
< Content-Type: text/html
< Content-Length: 146
< Connection: keep-alive
< 
<html>
<head><title>404 Not Found</title></head>
<body>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx</center>
</body>
</html>
* Connection #0 to host kolay.ne left intact

$ curl --resolve "kolay.ne:80:$( minikube ip )" --verbose http://kolay.ne/time ; echo
* Added kolay.ne:80:192.168.49.2 to DNS cache
* Hostname kolay.ne was found in DNS cache
*   Trying 192.168.49.2:80...
* Connected to kolay.ne (192.168.49.2) port 80
> GET /time HTTP/1.1
> Host: kolay.ne
> User-Agent: curl/8.7.1
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 200 OK
< Date: Fri, 29 Mar 2024 13:58:51 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 60
< Connection: keep-alive
< 
* Connection #0 to host kolay.ne left intact
In MSK it's 16:57:49. Have you brushed your teeth today yet?
$ curl --resolve "kolay.ne:80:$( minikube ip )" --verbose http://kolay.ne/cats ; echo
* Added kolay.ne:80:192.168.49.2 to DNS cache
* Hostname kolay.ne was found in DNS cache
*   Trying 192.168.49.2:80...
* Connected to kolay.ne (192.168.49.2) port 80
> GET /cats HTTP/1.1
> Host: kolay.ne
> User-Agent: curl/8.7.1
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 200 OK
< Date: Fri, 29 Mar 2024 13:58:56 GMT
< Content-Type: text/plain; charset=utf-8
< Content-Length: 162
< Connection: keep-alive
< 
* Connection #0 to host kolay.ne left intact
There is a species of cat smaller than the average housecat. It is native to Africa and it is the Black-footed cat (Felis nigripes). Its top weight is 5.5 pounds.
$
```

Note: 5.5 pounds is about 2.49 kilograms
