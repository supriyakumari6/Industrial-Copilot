# System Architecture

## Current

Sensor Data
    ↓
Preprocessing
    ↓
ML Baseline
    ↓
Prediction

## Target

Sensor Data
    ↓
ML/DL Anomaly Detection
    ↓
Anomaly Context
    ↓
RAG Retrieval
    ↓
Qdrant
    ↓
Ollama LLM
    ↓
Diagnosis
    ↓
FastAPI
    ↓
Dashboard

## MLOps

Training
    ↓
MLflow
    ↓
Evaluation
    ↓
Model Registry
    ↓
Docker
    ↓
Deployment
