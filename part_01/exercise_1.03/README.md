
## Build and Push Docker Image

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Build Docker Image:**
   ```bash
   docker build -t <dockerhub-username>/log-output:latest .
   ```

3. **Login to Docker Hub:**
   ```bash
   docker login
   ```

4. **Push Docker Image to Docker Hub:**
   ```bash
   docker push <dockerhub-username>/log-output:latest
   ```

## Deploy to Kubernetes

1. **Update deployment.yaml:**
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: log-output
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: log-output
     template:
       metadata:
         labels:
           app: log-output
       spec:
         containers:
         - name: log-output
           image: nirmalnaveen/log-output
           ports:
           - containerPort: 80
   ```

2. **Apply Deployment to Kubernetes:**
   ```bash
   kubectl apply -f deployment.yaml
   ```

3. **Check Pod Status:**
   ```bash
   kubectl get pods
   ```

## Check Logs

1. **List Running Pods:**
   ```bash
   kubectl get pods
   ```

2. **Check Logs for Specific Pod:**
   ```bash
   kubectl logs -f <pod-name>
   ```
   Example:
   ```bash
   kubectl logs -f log-output-574b4675d5-n67fl
   ```

## Troubleshooting

- **Pod Not Running:**
  ```bash
  kubectl describe pod <pod-name>
  ```
  Check for errors under `Events`.

- **Restart Pod:**
  ```bash
  kubectl delete pod <pod-name>
  ```
  Kubernetes will automatically recreate the pod.

- **Check Cluster Status:**
  ```bash
  kubectl cluster-info
  kubectl get nodes
  ```

- **Force Apply without Validation:**
  ```bash
  kubectl apply -f deployment.yaml --validate=false
  ```

## Conclusion
This project demonstrates how to containerize and deploy a simple application to Kubernetes, providing insight into logging and monitoring through Kubernetes CLI.

