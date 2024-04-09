# Helm

## Task 1

Initially, I create an chart app-python by using:
`helm create app-python`

Then, start minikube by using:
`minikube start`

After successfull starting of the minikube I can install app-python by using:
`helm install app-python app-python`

![img.png](./screenshots/helm_start.png)

To show the page in the browser I can run: `minikube service app-python`

![img.png](./screenshots/helm_serv.png)

Now we can see the output:
`kubectl get pods,svc`

![img.png](./screenshots/helm_info.png)

And also a workload page in the dashboard:
`minikube dashboard`

![img.png](./screenshots/workloads_helm.png)

## Task 2

At first, we need to create to files `post-install-hook.yaml` and `pre-install-hook.yaml`

Next, we can run the following command `helm lint app-python/` and see the following output:

![img.png](./screenshots/t2_1.png)

Then, we can run `helm install --dry-run helm-hooks app-python` to debug:

![img.png](./screenshots/t2_2.png)
![img.png](./screenshots/t2_3.png)

Next, run `kubectl get po` to get all pods: 

![img.png](./screenshots/kub_po.png)

Next, run `kubectl describe po postinstall-hook` to get info about post-install hook: 

![img.png](./screenshots/kub_post.png)

Next, run `kubectl describe po preinstall-hook` to get info about pre-install hook: 

![img.png](./screenshots/kub_pre.png)

To make a delete policy we can add the following `"helm.sh/hook-delete-policy": hook-succeeded` in the annotations field in .yaml hooks files

![img.png](./screenshots/kub_del.png)
