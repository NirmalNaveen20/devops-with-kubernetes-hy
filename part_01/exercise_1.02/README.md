# Part 1 Exercise 2 - Todo-App

Todo-app located in `/apps/todo-app` at commit [https://github.com/nirmalnaveen/kubernetes-devops/commit/<commit-id>](https://github.com/nirmalnaveen/kubernetes-devops/commit/<commit-id>). Published through Docker Hub at `nirmalnaveen/todo-app`.

## Deployment

1. **Create the deployment** with the following command:
   ```bash
   kubectl create deployment todo-app --image=nirmalnaveen/todo-app:latest

2. **Get pods** with the following command:
   ```bash
   kubectl get pods

3. **See logs with** with the following command:
   ```bash
   kubectl logs -f todo-app-dep-5f46796d5b-4nxx9