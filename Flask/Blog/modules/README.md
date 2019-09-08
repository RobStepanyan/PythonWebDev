# Blog App

## Requirement of every file & folder

- index.py: This is the entry point of our flask web-server.
- requirements.txt: This file contains all required python modules.
- Dockerfile: This file is to build the docker container
- docker-compose.yml & docker-compose.prod.yml: Deployment configuration for both development & production environment.
- modules: This directory contains all the modules including app, logger etc.
- app: This directory will contain all the related controllers and other routes useful for our web application.
- dist: This directory will contain our front-end static files like index.html & other JS files
- logger: This is wrapper module over python logging module.