
 Fullstack Skeletal Flask + React App with Kubernetes and ArgoCD

## Project Overview

This project demonstrates a fullstack application consisting of a React frontend and a Flask backend. Both components are containerized using Docker and deployed on a Kubernetes cluster. ArgoCD is integrated to implement GitOps workflows, making Git the single source of truth for infrastructure and application deployment management.

---




## How I Built This Project

This project is a fullstack web application featuring a React frontend and a Flask backend, containerized with Docker and deployed on a Kubernetes cluster. To automate and manage deployments, I integrated GitOps workflows using ArgoCD.

### Frontend Setup

- Created the React app using the official create-react-app script for a fast and standard setup.
- Installed necessary dependencies such as React Router and Axios.
- Built the core user interface in `src/App.js` and handled DOM rendering with `index.js`.
- Styled components with CSS for a clean, responsive UI.

### Backend Setup

- Developed the backend API using Flask, a lightweight Python web framework.
- Managed cross-origin requests by enabling CORS to allow React frontend communication.
- Created a simple REST API endpoint `/api/items` that serves sample data as JSON.
- Defined dependencies in `requirements.txt` and installed them in a Python virtual environment.
- Wrote the Flask application in `app.py` with clean, readable routes.

### Containerization & Deployment

- Dockerized both frontend and backend services with individual Dockerfiles.
- Built and pushed Docker images to Docker Hub via a GitHub Actions workflow, enabling CI/CD automation.


## Key Issue: Deployment Configuration Drift Between GitHub and Kubernetes Cluster

### Description

During deployment validation, I discovered a mismatch between the Kubernetes cluster’s running state and the expected configuration stored in the GitHub repository:

- Running `kubectl get deployments` on the local cluster showed:

  ```bash
  NAME            READY   UP-TO-DATE   AVAILABLE   AGE
  flask-backend   2/2     2            2           5d5h

  Only 2 pods were running.

The deployment.yaml in the devops-feature branch of GitHub specified: replicas: 3
Expecting 3 pods to be running.

Root Cause
The Kubernetes cluster was running an outdated deployment configuration, not matching the latest manifests in GitHub. This caused fewer pods than intended to run.

Resolution Steps
Re-applied the updated deployment configuration:


kubectl apply -f deployment.yaml
Verified updated deployment status:
kubectl get deployments


flask-backend   3/3   3   3   AGE


## Integrating GitOps with ArgoCD

To enforce consistency and automate deployments, I integrated ArgoCD for GitOps management.

### Setup Process

- Created an ArgoCD Application linked to the GitHub repository and target branch.
- Added Kubernetes manifests to a dedicated `agroyaml/` directory.
- Updated the deployment manifest (`deploy.yaml`) specifying desired replicas (e.g., 3 or 4).
- Pushed changes to the GitHub repository:

```bash
git add deploy.yaml
git commit -m "Update pod replicas"
git push origin devops-feature


Enabled auto-sync in the ArgoCD UI, which automatically reconciled the Kubernetes cluster state to match the Git repository, adjusting the number of pods accordingly.

### Accessing ArgoCD UI

Forward ArgoCD server port locally:
kubectl port-forward svc/argocd-server -n argocd 8080:443
Retrieve the initial admin password:
kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64
Visit https://localhost:8080 in your browser and login.

## Challenges and Learnings

### Conflict Between ArgoCD Installation and Python Virtual Environment (venv)

**Problem:**  
Installation failed due to symbolic link errors caused by the active Python `venv` directory.

**Solution:**  
- Added `venv/` to `.gitignore` to exclude it from Git tracking:

echo "venv/" >> .gitignore

Deactivated the virtual environment before installation.

Lesson:
Isolating environment-specific directories prevents conflicts during infrastructure tool setup.

What I Learned
Cluster State Synchronization: Always ensure Kubernetes manifests in Git match the cluster state to avoid drift.

Power of GitOps: ArgoCD automates deployments and helps maintain a declarative and version-controlled infrastructure.

Best Practices: Proper environment isolation and version control hygiene improve collaboration and reduce errors.








## Project Overview

This project demonstrates deploying flask app to aws EKS 

---
 AWS Kubernetes Deployment Portfolio Projects


---

##  Flask App Deployment to AWS EKS

### Containerization & Deployment
 
- Dockerized both frontend and backend services with individual Dockerfiles.
- Built and pushed Docker images to Docker Hub via bash

Flask app — containerized with Docker  
Deployed to AWS EKS (Elastic Kubernetes Service)   Cluster created using eksctl   App deployed using kubectl
 Exposed via AWS Load Balancer

---

#  Why I built these projects

To demonstrate real-world Kubernetes and AWS EKS skills  
    

---

#  Technologies Used

- AWS EKS  
- Kubernetes (Pods, Services, )    
- Docker  
- eksctl  
- kubectl    
- Flask  
- React  

---

# Learnings and Challenges
--Automating EKS cluster creation
--After deploying to AWS EKS
--Got the external IP using (kubectl get svc my-app-service)
--Ran the loadbalancer link on a browser, it shows not reacheable
--went to the Nano app.py and edited the local host  to if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80) I edit it because in cloud you can’t use localhost  cloud traffic comes from outside!
 host='0.0.0.0' makes it reachable from LoadBalancer
After doing that it worked, the loadbalance link could then show the flask app content
  


