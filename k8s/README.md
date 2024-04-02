# Task 1: Kubernetes Setup and Basic Deployment

We've deployed our application within the Minikube cluster using the following steps:

1. Created a Deployment resource using `kubectl create deployment` command to define the desired state of our application.
2. Made our application accessible from outside the Kubernetes virtual network by creating a Service resource using `kubectl expose deployment` command.

![Alt text](screenshots/1.png?raw=true)

To maintain a tidy Kubernetes environment, we've removed the Deployment and Service resources that we created using `kubectl delete` command.

# Task 2: Declarative Kubernetes Manifests

We've adopted a more efficient and structured approach by employing configuration files to deploy our application:

- `deployment.yml`: Describes our application's deployment with at least 3 replicas using a Deployment resource.
- `service.yml`: Defines a Service resource for our application to make it accessible from outside the Kubernetes cluster.

![Alt text](screenshots/2.png?raw=true)
![Alt text](screenshots/3.png?raw=true)
