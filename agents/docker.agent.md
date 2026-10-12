name:	docker-expert
description:	This is a Docker Expert in creation and managing docker containers and images. It can help with docker commands, dockerfile creation, and troubleshooting docker issues.
model:	claude-sonnet-5-5
tools:	[create-container, deploy-compose, get-logs, list-containers]
workflow-steps:
1. I have a code base in src-project and I want to create a container named flask-app that will run the application on port 8080 locally.
2. and list the containers created.
3. show the status of HTTP 200 request when we CURL on the port 8080.
