# Introduction to Kubernetes

## Task 1

1. I deployed my application usig commands

   ```bash
   kubectl create deployment app-python --image ozurexus/my-flask-app
   kubectl expose deployment app-python --type=LoadBalancer --port=8080
   ```

   ![img.png](screenshots/terminal_deploy.png)

2. I used the following command to get accesible url to check deployment:

   ```bash
   minikube service app-python --url
   ```

   ![img.png](screenshots/terminal_result.png)

## Task 2

1. I wrote deployment.yml and service.yml and applied them. Screenshot from terminal:

   ![img.png](screenshots/yml_deploy.png)

2. Checking deploy in browser:

   ![img.png](screenshots/yml_result.png)
