# 🐳 Docker & FastAPI + Gradio Lab

A hands-on learning project covering Docker fundamentals, Dockerfile, containers, FastAPI, Gradio, Seaborn Titanic Dataset, and public web access using Cloudflare Tunnel.

This project was developed and tested on **macOS + Docker Desktop + Python Virtual Environment** as a Mac adaptation of the course exercises.

---

## 📚 What I Learned

Through this lab, I practiced:

- GitHub Codespaces concepts
- Docker fundamentals
- Docker Image and Container
- Dockerfile
- Building Docker Images
- Running Docker Containers
- Port Mapping
- Docker Desktop
- Python Virtual Environment
- FastAPI
- Uvicorn
- Gradio
- Seaborn Titanic Dataset
- Mounting Gradio into FastAPI
- Public web access with Cloudflare Tunnel
- Testing applications through a Private Browser Window

---

# 🧪 Exercise 1 — Dockerfile & Nginx

## 🎯 Objective

Create a simple HTML webpage, package it into a Docker Image using a Dockerfile, run it as a container, and access the webpage through a browser.

---

## 📁 Project Structure

```text
my-docker-test/
│
├── docker-lab/
│   ├── Dockerfile
│   └── index.html
│
├── fastapi-gradio-lab/
│   ├── app.py
│   └── .venv/
│
├── Dockerfile
└── app.py
