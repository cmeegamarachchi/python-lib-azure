FROM mcr.microsoft.com/devcontainers/typescript-node:20-bullseye

# Install Azure CLI
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# Install Azure Static Web Apps CLI
RUN npm install -g @azure/static-web-apps-cli && \
npm install -g azure-functions-core-tools@4 --unsafe-perm true

# Install python
RUN apt-get update && \
	apt-get install -y python3-pip python-dev build-essential && \
	npm install --global prettier && \
	pip install black&& \
	npm upgrade --global yarn