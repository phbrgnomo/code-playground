#!/bin/bash

current_directory=$(basename "$PWD")

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Building Docker container for project in $current_directory${NC}"

# Parse command line parameters
build_engine=$1

# Check if a second parameter is provided
if [ -n "$2" ]; then
    dockerfile_type="$2"
fi

# Set default Dockerfile type if not provided
if [ -z "$dockerfile_type" ]; then
    dockerfile_type="Dockerfile"
    echo -e "${YELLOW}No context provided. Using Dockerfile${NC}"

else
    dockerfile_type="$dockerfile_type.Dockerfile"
    echo -e "Using ${YELLOW}$dockerfile_type${NC} as context."
fi

# Switch based on the build engine specified
case "$build_engine" in
    "dockerfile")
        # Use the project directory name as the container name (lowercase)
        container_name=$(echo "$current_directory" | tr '[:upper:]' '[:lower:]')

        # Remove all existing containers with the same name
        echo -e "Removing existing containers with the name: ${YELLOW}$container_name${NC}"
        docker rm -f $(docker ps -aqf "name=$container_name") || true

        # Remove all images with the same name
        echo -e "Removing existing images with the name: ${YELLOW}$container_name${NC}"
        docker rmi -f $(docker images -q $container_name) || true


        # Extract WORKDIR from Dockerfile
        container_workdir=$(awk '/WORKDIR/ {gsub(/["'\'']/, "", $2); print $2}' "$dockerfile_type" | tr -d '[:space:]' | sed 's|^/||')

        # Build Docker image
        echo -e "Building Docker image: ${YELLOW}$container_name${NC}"
        docker build -t "$container_name" -f "$dockerfile_type" .

        # Run the container
        echo -e "Running Docker container: ${YELLOW}$container_name${NC}"
        # docker run -d --name "$container_name" "$container_name"
        # echo "docker run -d --name '$container_name' -w '/$container_workdir' -e USER_NAME=$USER_NAME '$container_name'"
        docker run -d -v "$(pwd):/$container_workdir" --name "$container_name" -w "/$container_workdir" "$container_name"
        # echo "docker run -d -v \"\$(pwd):/$container_workdir\" --name \"$container_name\" -w \"/$container_workdir\" \"$container_name\""
        # echo "container_workdir=$container_workdir"
        # echo "USER_NAME=$USER_NAME"
        ;;

    "compose")
        # Check if docker-compose.yml exists
        if [ -f docker-compose.yml ]; then
            container_name=$(grep -oP 'container_name:\s*\K\w+' docker-compose.yml)
            if [ -n "$container_name" ]; then
                # Remove all existing containers with the same name
                echo -e "Removing existing containers with the name: ${YELLOW}$container_name${NC}"
                docker-compose down || true

                # Remove all images with the same name
                echo -e "Removing existing images with the name: ${YELLOW}$container_name${NC}"
                docker rmi -f $(docker images -q $container_name) || true

                # Bring up the Docker Compose services
                echo -e "Bringing up Docker Compose services"
                docker-compose up -d
            else
                echo -e "${RED}Error: Unable to determine container name from docker-compose.yml. Make sure 'container_name' is defined.${NC}"
            fi
        else
            echo -e "${RED}Error: docker-compose.yml not found. Please make sure it exists in the project directory.${NC}"
        fi
        ;;

    *)
        echo -e "${RED}Error: Invalid build engine. Use 'dockerfile' or 'compose'.${NC}"
        exit 1
        ;;
esac

# Final instructions for VS Code Dev Containers plugin
echo -e "----------------------------------------------------------------------------------------"
echo -e "\nTo open this container in VS Code with the Dev Containers extension:"
echo -e "1. Install the 'Remote - Containers' extension in VS Code."
echo -e "2. Run 'Dev Containers: Attach to Running Container' from the command palette."
echo -e "3. Select the container you want to work on.\n"
echo -e "----------------------------------------------------------------------------------------"

echo -e "${GREEN}Build process completed.${NC}"
