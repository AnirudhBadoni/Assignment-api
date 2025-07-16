# Demo FastAPI DevOps Challenge

This project demonstrates a simple FastAPI web service with Dockerization, CI/CD pipeline, Helm packaging, and Kubernetes deployment.

---

## Features

- FastAPI app exposing `/api` POST endpoint showing request headers, method, and body  
- Prometheus metrics exposed at `/metrics`  
- Dockerized with best practices  
- CI/CD using GitHub Actions (build & test)  
- Helm chart for Kubernetes deployment  

---

## Prerequisites

- Python 3.10+  
- Docker  
- Kubernetes cluster (Minikube, k3d, GKE, etc.)  
- Helm 3+  
- kubectl CLI  
- Docker Hub account (for image hosting)  

---

## Local Development

1. Create and activate a virtual environment (optional but recommended):

   ```
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
   ```
   pip install -r requirements.txt

3. Run the FastAPI app:
   ```
   uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
   
4. Test API:
   ```   
   curl -X POST http://localhost:8000/api -H "Content-Type: application/json" -d '{"username":"xyz","password":"xyz"}'
   
5. Test Prometheus metrics:
   ```
   curl http://localhost:8000/metrics

## Docker
1. Build Docker image:
   ```
   docker build -t fastapi-demo-api:latest .
   
2. Run container:
   ```
   docker run -d -p 8000:8000 fastapi-demo-api
   
3. Test as above via localhost:8000.

   
## Docker Hub

1. Tag the image:
   ```
   docker tag fastapi-demo-api:latest YOUR_DOCKERHUB_USERNAME/fastapi-demo-api:latest
   
2. Login and push:
   ```
   docker login
   docker push YOUR_DOCKERHUB_USERNAME/fastapi-demo-api:latest
   
3. Update charts/demo-api/values.yaml:
   ```
   yaml
   image:
      repository: YOUR_DOCKERHUB_USERNAME/fastapi-demo-api
      tag: latest

## Kubernetes Deployment with Helm
1. Install Helm chart:
   ```
   helm install demo-api charts/demo-api

2. Verify deployment:
   ```
   kubectl get pods,svc

3. Port-forward to test API:
   ```
   kubectl port-forward svc/demo-api 8000:8000
   curl -X POST http://localhost:8000/api -H "Content-Type: application/json" -d '{"username":"xyz","password":"xyz"}'

## CI/CD
- GitHub Actions workflow in .github/workflows/ci-cd.yml

- Automatically builds and tests code on push/pull requests

- Builds Docker image (optionally can be extended to push to registry)

## TODOs / Improvements
- Add unit and integration tests for API

- Add container structure tests

- Extend CI/CD to push Docker image and deploy Helm chart automatically

- Add monitoring & alerting (Grafana dashboards)

- Implement more OPA policies for enhanced security


