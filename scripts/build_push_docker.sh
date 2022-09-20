#!/bin/sh
docker login

# Backend
docker build -t udaobsrv-backend ./reference-app/backend
docker tag udaobsrv-backend:latest jeikens/udaobsrv-backend:v2
docker push jeikens/udaobsrv-backend:v2

# Frontend
docker build -t udaobsrv-frontend ./reference-app/frontend
docker tag udaobsrv-frontend:latest jeikens/udaobsrv-frontend:v2
docker push jeikens/udaobsrv-frontend:v2

# Trial
docker build -t udaobsrv-trial ./reference-app/trial
docker tag udaobsrv-trial:latest jeikens/udaobsrv-trial:v2
docker push jeikens/udaobsrv-trial:v2