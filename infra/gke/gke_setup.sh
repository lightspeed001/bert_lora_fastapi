# Build and push Docker image to Google Container Registry
docker build -t gcr.io/YOUR_PROJECT_ID/lora-bert-fastapi:latest .
gcloud auth configure-docker
docker push gcr.io/YOUR_PROJECT_ID/lora-bert-fastapi:latest

# Create a GKE cluster with GPU nodes (if needed)
gcloud container clusters create lora-bert-cluster \
    --num-nodes=3 \
    --machine-type=n1-standard-4 \
    --accelerator=type=nvidia-tesla-t4,count=1 \
    --zone=us-central1-a

# Apply the deployment
kubectl apply -f gke-deployment.yaml

# Get the external IP
kubectl get service lora-bert-service

