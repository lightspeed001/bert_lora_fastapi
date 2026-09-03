# Start Minikube with GPU support if needed
minikube start --driver=docker --gpus=1

# Load Docker image into Minikube
minikube image load lora-bert-fastapi:latest

# Apply the deployment
kubectl apply -f minikube-deployment.yaml

# Access the service
minikube service lora-bert-service

