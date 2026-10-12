# feature-branch

## Purpose

This branch adds a small Flask app that runs on port 8080 and returns the hostname of the machine (or container) it runs on. It is packaged with a Dockerfile so it can be run as a container. The app is used to show that a container is serving HTTP and which container answered the request.

## HTTP status

Request: `curl http://localhost:8080/`

Result: **HTTP 200**

Response body:

```
Hostname: dc2924fe026d
```

## Steps taken

1. Wrote `src-project/app.py`: a Flask app with a single route `/` that returns `socket.gethostname()`, listening on `0.0.0.0:8080`.
2. Wrote `src-project/requirments.txt` with `flask==3.0.3` and `src-project/Dockerfile` based on `python:3.12-slim`.
3. Built the image: `docker build -t hostname-app .` in `src-project/`.
4. Created the container `flask-app` from the image with port 8080 mapped to 8080.
5. Confirmed the container is running with `docker ps` (listed as `flask-app`).
6. Sent `curl` to `http://localhost:8080/` and received HTTP 200.
7. Created this branch from `main` and added this `readme.md`.
8. Created the public GitHub repository `ai-agent-subagents-lab1` and pushed `main` and `feature-branch` to it.
