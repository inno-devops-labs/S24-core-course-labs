# Lab 14

## Components

1. **Prometheus Operator**:
    - Manages Prometheus instances in Kubernetes.
    - Automates deployment, configuration, and management.

2. **Prometheus**:
    - Time-series database and monitoring system.
    - Collects metrics by scraping HTTP endpoints.
    - Stores metrics and allows real-time querying.

3. **Alertmanager**:
    - Handles alerts from Prometheus.
    - Deduplicates, groups, and routes alerts to receivers.
    - Supports silencing alerts and various notification channels.

4. **Grafana**:
    - Visualization tool for creating dashboards and graphs.
    - Pre-configured with dashboards for monitoring Kubernetes and Prometheus.

5. **kube-state-metrics**:
    - Provides Kubernetes objects' state information.
    - Exposes metrics for Prometheus scraping.

6. **node-exporter**:
    - Agent deployed on each Kubernetes node.
    - Collects system-level metrics like CPU, memory, disk usage, etc.
    - Exposes metrics for Prometheus scraping.

7. **Prometheus Adapter**:
    - Allows Prometheus metrics querying as custom metrics in Kubernetes.
    - Enables features like horizontal pod autoscaling (HPA) based on custom metrics.

## `kubectl get po,sts,svc,pvc,cm`

```
djovi@djovi-NBD-WXX9:~/PycharmProjects/S24-core-course-labs/k8s$ kubectl get po,sts,svc,pvc,cm
NAME                                                            READY   STATUS    RESTARTS      AGE
pod/alertmanager-kube-prometheus-stack-alertmanager-0           2/2     Running   0             4m44s
pod/app-python-0                                                1/1     Running   0             3m
pod/app-python-1                                                1/1     Running   0             2m59s
pod/kube-prometheus-stack-grafana-7cf5785ff8-rkzcf              3/3     Running   0             4m44s
pod/kube-prometheus-stack-kube-state-metrics-65594f9476-8g4jh   1/1     Running   0             4m44s
pod/kube-prometheus-stack-operator-6b55ff594d-57p2k             1/1     Running   0             4m44s
pod/kube-prometheus-stack-prometheus-node-exporter-66hqh        1/1     Running   0             4m44s
pod/prometheus-kube-prometheus-stack-prometheus-0               2/2     Running   0             4m44s

NAME                                                               READY   AGE
statefulset.apps/alertmanager-kube-prometheus-stack-alertmanager   1/1     4m44s
statefulset.apps/app-python                                        2/2     3m
statefulset.apps/prometheus-kube-prometheus-stack-prometheus       1/1     4m44s

NAME                                                     TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
service/alertmanager-operated                            ClusterIP   None             <none>        9093/TCP,9094/TCP,9094/UDP   4m44s
service/app-python                                       NodePort    10.100.155.107   <none>        5000:31145/TCP               3m
service/kube-prometheus-stack-alertmanager               ClusterIP   10.104.191.47    <none>        9093/TCP,8080/TCP            4m44s
service/kube-prometheus-stack-grafana                    ClusterIP   10.111.146.229   <none>        80/TCP                       4m44s
service/kube-prometheus-stack-kube-state-metrics         ClusterIP   10.108.8.21      <none>        8080/TCP                     4m44s
service/kube-prometheus-stack-operator                   ClusterIP   10.102.240.42    <none>        443/TCP                      4m44s
service/kube-prometheus-stack-prometheus                 ClusterIP   10.108.52.211    <none>        9090/TCP,8080/TCP            4m44s
service/kube-prometheus-stack-prometheus-node-exporter   ClusterIP   10.110.190.20    <none>        9100/TCP                     4m44s
service/kubernetes                                       ClusterIP   10.96.0.1        <none>        443/TCP                      33d
service/prometheus-operated                              ClusterIP   None             <none>        9090/TCP                     4m44s

NAME                                      STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/data-app-python-0   Bound    pvc-4dfea5e6-dfb8-4d36-a3ae-5ef2d1ae0d62   1Gi        RWO            standard       4d
persistentvolumeclaim/data-app-python-1   Bound    pvc-cd5e8522-e4a6-44ad-99ea-b6ff85f80d24   1Gi        RWO            standard       4d

NAME                                                                DATA   AGE
configmap/configmap                                                 2      3m
configmap/kube-prometheus-stack-alertmanager-overview               1      4m44s
configmap/kube-prometheus-stack-apiserver                           1      4m44s
configmap/kube-prometheus-stack-cluster-total                       1      4m44s
configmap/kube-prometheus-stack-controller-manager                  1      4m44s
configmap/kube-prometheus-stack-etcd                                1      4m44s
configmap/kube-prometheus-stack-grafana                             1      4m44s
configmap/kube-prometheus-stack-grafana-config-dashboards           1      4m44s
configmap/kube-prometheus-stack-grafana-datasource                  1      4m44s
configmap/kube-prometheus-stack-grafana-overview                    1      4m44s
configmap/kube-prometheus-stack-k8s-coredns                         1      4m44s
configmap/kube-prometheus-stack-k8s-resources-cluster               1      4m44s
configmap/kube-prometheus-stack-k8s-resources-multicluster          1      4m44s
configmap/kube-prometheus-stack-k8s-resources-namespace             1      4m44s
configmap/kube-prometheus-stack-k8s-resources-node                  1      4m44s
configmap/kube-prometheus-stack-k8s-resources-pod                   1      4m44s
configmap/kube-prometheus-stack-k8s-resources-workload              1      4m44s
configmap/kube-prometheus-stack-k8s-resources-workloads-namespace   1      4m44s
configmap/kube-prometheus-stack-kubelet                             1      4m44s
configmap/kube-prometheus-stack-namespace-by-pod                    1      4m44s
configmap/kube-prometheus-stack-namespace-by-workload               1      4m44s
configmap/kube-prometheus-stack-node-cluster-rsrc-use               1      4m44s
configmap/kube-prometheus-stack-node-rsrc-use                       1      4m44s
configmap/kube-prometheus-stack-nodes                               1      4m44s
configmap/kube-prometheus-stack-nodes-darwin                        1      4m44s
configmap/kube-prometheus-stack-persistentvolumesusage              1      4m44s
configmap/kube-prometheus-stack-pod-total                           1      4m44s
configmap/kube-prometheus-stack-prometheus                          1      4m44s
configmap/kube-prometheus-stack-proxy                               1      4m44s
configmap/kube-prometheus-stack-scheduler                           1      4m44s
configmap/kube-prometheus-stack-workload-total                      1      4m44s
configmap/kube-root-ca.crt                                          1      33d
configmap/prometheus-kube-prometheus-stack-prometheus-rulefiles-0   35     4m43s
```

### Pods

The components responsible for orchestrating the tasks outlined earlier include Alertmanager, Grafana,
kube-state-metrics, node-exporter, Prometheus Adapter, and Prometheus Operator. These components collectively manage the
execution of all essential services.

### Stateful Sets

Stateful Sets are utilized for Prometheus and Alertmanager to ensure persistent storage, enabling them to store metrics
and alert metadata reliably.

### Services

Services such as Alertmanager, Blackbox Exporter, Grafana, kube-state-metrics, node-exporter, Prometheus Adapter, and
Prometheus-k8s facilitate the navigation and interaction among the various components of the monitoring stack as
described previously.

### Config Maps
Config Maps like env-config-map, python-app-configmap, adapter-config, and prometheus-k8s-rulefiles-0 are employed to
store configurations for Prometheus, Grafana, Alertmanager, and other services within the monitoring stack, ensuring
seamless operation and management.


## Answers for the questions:
1. CPU consumption: 3%, memory consumption: 1.3GB
2. kube-apiserver has the highest CPU usage,  app-python has the lowest CPU usage
3. Memory usage: 5,1GB; 36%
4. I have 18 pods and 37 containers
5. Download speed: 19.8 kB/s Upload speed: 93 kB/s
6. 8 alerts


