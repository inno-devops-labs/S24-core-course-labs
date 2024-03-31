# Lab 13: Kubernetes StatefulSet

## Overview

In this lab, you'll explore Kubernetes StatefulSets, focusing on managing stateful applications with guarantees about the ordering and uniqueness of a set of Pods.

## Task 1: Implement StatefulSet in Helm Chart

**6 Points:**

1. Understand StatefulSets:
   - Read about StatefulSet objects:
     - [Concept](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
     - [Tutorial](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/)

2. Update Helm Chart:
   - Rename `deployment.yml` to `statefulset.yml`.
   - Create a manifest for StatefulSet following the tutorial.
   - Test with command: `helm install --dry-run --debug name_of_your_chart path_to_your_chart`.
   - Fix any issues and deploy it.
   - Apply best practices by moving values to variables in `values.yml` meaningfully.

## Task 2: StatefulSet Exploration and Optimization

**4 Points:**

1. Research and Documentation:
   - Create `13.md` report.
   - Include the output of `kubectl get po,sts,svc,pvc` commands.
   - Use `minikube service name_of_your_statefulset` command to access your app.
   - Access the root path of your app from different tabs and modes in your browser.
   - Check the content of your file in each pod, e.g., `kubectl exec pod/demo-0 -- cat visits`, and provide the output for all replicas.
   - Describe and explain differences in the report.

2. Ordering Guarantee and Parallel Operations:
   - Explain why ordering guarantees are unnecessary for your app.
   - Implement a way to instruct the StatefulSet controller to launch or terminate all Pods in parallel.

**List of Requirements:**

- Outputs of commands in `13.md`.
- Results of the "number of visits" command for each pod, with an explanation in `13.md`.
- Answers to questions in point 2 of `13.md`.
- Implementation of parallel launch and terminate.

## Bonus Task: Update Strategies

**2.5 Points:**

1. Apply the main steps to your extra app.
2. Explore Update Strategies:
   - Read about update strategies.
   - Describe your understanding of kinds and differences in the report.

**Guidelines:**

- Maintain clear and organized documentation.
- Use appropriate naming conventions for files and folders.
- For your repository PR, ensure it's from the `lab13` branch to the main branch.

> Note: Understanding StatefulSets and their optimization is crucial for managing stateful applications in Kubernetes. Explore the bonus tasks to further enhance your skills.
