# Trade Order Backend Service

This project is a simple backend service built with **FastAPI** (Python) that exposes REST APIs for managing trade orders. It also includes WebSocket support for real-time order status updates. The application is containerized using **Docker**, deployed on an **AWS EC2 instance**, and integrated with a **CI/CD pipeline** using **GitHub Actions**.

---

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Setup and Installation](#setup-and-installation)
4. [Running the Application](#running-the-application)
5. [Deployment to AWS EC2](#deployment-to-aws-ec2)
6. [CI/CD Pipeline with GitHub Actions](#cicd-pipeline-with-github-actions)
7. [API Documentation](#api-documentation)
8. [WebSocket Support](#websocket-support)
9. [Troubleshooting](#troubleshooting)
10. [Contributing](#contributing)

---

## Features
- **REST APIs**:
  - `POST /orders`: Submit a new trade order.
  - `GET /orders`: Retrieve a list of submitted orders.
- **WebSocket Support**: Real-time updates for order status changes.
- **Database**: SQLite for development, PostgreSQL for production.
- **Containerization**: Docker for easy deployment.
- **Deployment**: Hosted on AWS EC2.
- **CI/CD**: Automated testing and deployment using GitHub Actions.

---

## Technologies Used
- **Backend**: FastAPI (Python)
- **Database**: SQLite (Development), PostgreSQL (Production)
- **Containerization**: Docker
- **Deployment**: AWS EC2
- **CI/CD**: GitHub Actions
- **WebSocket**: FastAPI WebSocket support

---

## Setup and Installation

### Prerequisites
- Python 3.9+
- Docker
- AWS Account (for EC2 deployment)
- GitHub Account (for CI/CD)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/trade-order-backend.git
   cd trade-order-backend