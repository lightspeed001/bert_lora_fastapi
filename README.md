# bert_lora_fastapi
## Deploying a LoRA-optimized BERT model as a FastAPI service with Minikube and GKE

### 1. High-Level System Architecture

```mermaid
graph TD
    A[Client] -->|HTTP Request| B[GKE Load Balancer]
    B --> C[GKE Ingress Controller]
    C --> D[FastAPI Service Pod 1]
    C --> E[FastAPI Service Pod 2]
    C --> F[FastAPI Service Pod 3]
    D --> G[LoRA-optimized BERT Model]
    E --> G
    F --> G
    G --> H[GPU Node Pool]
    I[Cloud Storage] -->|Model Weights| G

```
> __Components__
- __Client__: End user or application making requests
- __GKE Load Balancer__: Distributes traffic across ingress controllers
- __GKE Ingress Controller__: Routes traffic to appropriate pods
- __FastAPI Service Pods__: Containerized FastAPI instances (3 replicas)
- __LoRA-optimized BERT model__: ML model loaded in memory
- __GPU Node Pool__: GKE nodes with GPU acceleration
- __Cloud Storage__: Where the model weights are stored (GCS bucket)

---

### 2. Detailed Kubernetes Architecture

```mermaid
graph TD
    A[Client Request] --> B[GKE Service]
    B --> C[Kubernetes Ingress]
    C --> D[FastAPI Deployment]
    D --> E[Pod 1]
    D --> F[Pod 2]
    D --> G[Pod 3]
    E --> H[Container]
    F --> H
    G --> H
    H --> I[LoRA BERT Model]
    H --> J[GPU Resources]
    K[GCS Bucket] -->|Model Sync| I

```
> __Components__
- __GKE Service__: Kubernetes Service exposing the FastApi deployment
- __Kubernetes Ingress__: Manages external access to the service
- __FastAPI Deployment__: Manages the 3 replicas of your application
- __Pods__: Individual containers running the FastAPI app
- __Container__: Docker container with the FastAPI app
- __LoRA BERT Model__: The actual ML model loaded in memory
- __GPU Resources__: GPU allocation for the pods
- __GCS Bucket__: Google Cloud Storage for modal weights

---

### 3. Data Flow Diagram

```mermaid
sequenceDiagram
    participant Client
    participant GKE_LB as GKE Load Balancer
    participant Ingress
    participant Pod1 as FastAPI Pod 1
    participant Model as LoRA BERT Model
    participant GPU as GPU Resources
    participant GCS as GCS Bucket

    Client->>GKE_LB: HTTP Request
    GKE_LB->>Ingress: Route Request
    Ingress->>Pod1: Forward Request
    Pod1->>Model: Process Request
    Model->>GPU: Use GPU Acceleration
    GPU-->>Model: Return Results
    Model-->>Pod1: Return Predictions
    Pod1-->>Client: HTTP Response
    GCS->>Model: Sync Model Weights (on startup)

```
> __Flow__
- Client sends HTTP request to GKE Load Balancer
- Load Balancer routes to Ingress Controller
- Ingress routes to one of ther FastAPI pods
- Pod loads the LoRA BERT model (syncing weights from GCS if needed)
- Model uses GPU acceleration for inference
- Results are returned through the same path



