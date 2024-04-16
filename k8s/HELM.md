# Helm

### Task 1

1. Check via `kubectl get pods,svc` command:

![](./screens/helm.png)

# Task 2: Helm hooks

## Helm Chart Hooks

### Lint the Helm chart
![](./screens/lint.png)

### Perform dry-run of the Helm chart
![](./screens/dry-run1.png)
![](./screens/dry-run2.png)

### Verify the Helm chart hooks
- `kubectl get po`
![](./screens/po.png)

- `kubectl describe po preinstall-hook`
![](./screens/pre1.png)
![](./screens/pre2.png)
- `kubectl describe po postinstall-hook`
![](./screens/post1.png)
![](./screens/post2.png)

### After adding hook delete policy, only webapp is running
- `kubectl get pods,svc`
![](./screens/helm-del.png)