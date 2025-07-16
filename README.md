# Demo FastAPI DevOps Challenge

This project demonstrates a simple FastAPI web service with Dockerization, CI/CD pipeline, Helm packaging, Kubernetes deployment, and Open Policy Agent (OPA) integration.

---

## Features

- FastAPI app exposing `/api` POST endpoint showing request headers, method, and body  
- Prometheus metrics exposed at `/metrics`  
- Dockerized with best practices  
- CI/CD using GitHub Actions (build & test)  
- Helm chart for Kubernetes deployment  
- Open Policy Agent (OPA) policy enforcing security best practices  

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

1. Create and activate virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
