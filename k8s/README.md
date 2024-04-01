## Kubernetes

### Kubernetes Setup

1. Deploy Application
    ```commandline
    kubectl create deployment app-python --image=monykekker/my_app:latest --port=8080
    ```
2. Access Application
    ```commandline
    kubectl expose deployment app-python --type=LoadBalancer --port=8080 
    ```

3. Output of `kubectl get pods,svc  `

    ```commandline
   NAME                                         READY   STATUS    RESTARTS   AGE
   pod/app-python-deployment-67d9ddb46d-glx8t   1/1     Running   0          2m25s
   pod/app-python-deployment-67d9ddb46d-mjklr   1/1     Running   0          2m25s
   pod/app-python-deployment-67d9ddb46d-q89p2   1/1     Running   0          2m25s
   
   NAME                         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
   service/app-python-service   LoadBalancer   10.108.78.82   localhost     8080:30093/TCP   2m18s
   service/kubernetes           ClusterIP      10.96.0.1      <none>        443/TCP          19m
    ```

4. Deploy using manifest
   ```commandline
   kubectl apply -f .\k8s\deployment.yml 
   kubectl apply -f .\k8s\service.yml
   ```

5. `minikube service --all`
   ```commandline
    W0401 13:52:09.870499   16716 main.go:291] Unable to resolve the current Docker CLI context "default": context "default": context not found: open C:\Users\Руслан\.docker\contexts\meta\37a8eec1ce19687d132fe29051dca629d164e2c4958ba141d5f4133a33f0688f\meta.json: The s
    ystem cannot find the path specified.
    |-----------|--------------------|-------------|---------------------------|
    | NAMESPACE |        NAME        | TARGET PORT |            URL            |
    |-----------|--------------------|-------------|---------------------------|
    | default   | app-python-service |        8000 | http://192.168.49.2:32152 |
    |-----------|--------------------|-------------|---------------------------|
    |-----------|------------|-------------|--------------|
    | NAMESPACE |    NAME    | TARGET PORT |     URL      |
    |-----------|------------|-------------|--------------|
    | default   | kubernetes |             | No node port |
    |-----------|------------|-------------|--------------|
    * service default/kubernetes has no node port
      * Starting tunnel for service app-python-service.
      * Starting tunnel for service kubernetes.
      |-----------|--------------------|-------------|------------------------|
      | NAMESPACE |        NAME        | TARGET PORT |          URL           |
      |-----------|--------------------|-------------|------------------------|
      | default   | app-python-service |             | http://127.0.0.1:56430 |
      | default   | kubernetes         |             | http://127.0.0.1:56432 |
      |-----------|--------------------|-------------|------------------------|
      * Opening service default/app-python-service in default browser...
      * Opening service default/kubernetes in default browser...
      ! Because you are using a Docker driver on windows, the terminal needs to be open to run it.
     ```

### Screenshot

![k8s](./k8s.png)