# Use the latest Ubuntu base image
FROM ubuntu:latest

# Upgrade existing packages, Install additional packages, and clean cache 
RUN apt-get update && \
    apt-get install -y \
        apt-utils \
        git \
        nano \
        tree \
        net-tools \
        jq \
        curl \
        wget \
        zsh && \
    apt-get full-upgrade -y &&\
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user use the same as the host user
ARG USER_NAME=host_username
ARG USER_ID=1000
ARG GROUP_ID=1000

RUN groupadd -g $GROUP_ID $USER_NAME && \
    useradd -u $USER_ID -g $GROUP_ID -m -s /bin/bash $USER_NAME

# Set the working directory. NOTE: Build.sh script will only work if you directly add the username, instead of the variable
WORKDIR /home/host_username/code_env

# Set correct permissions
RUN chmod -R 777 /home/$USER_NAME/code_env

# Switch to the non-root user
USER $USER_NAME

# Copy the current directory contents into the container
COPY --chown=$USER_NAME:$USER_NAME . .

# Volume build is handled on the docker run command line inside ./build.sh
# VOLUME /home/$USER_NAME/code_env

# Set the default command to keep the container running
CMD ["sh", "-c", "while true; do echo 'Container is running...'; sleep 10; done"]

