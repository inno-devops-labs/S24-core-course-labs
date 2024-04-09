### Task 1
`$ kubectl create deployment app-python --image=staglente/app_python:latest --port=5000`

`$ kubectl expose deployment app-python --type=LoadBalancer --port=5000`

`$ kubectl delete deployments app-python`
`$ kubectl delete services app-python`

### Task 2
`$ kubectl apply -f deployment.yml`
`$ kubectl apply -f service.yml`


