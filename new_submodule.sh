#!/bin/bash

# Script to set up a new GitHub repository, create a folder, and add it as a submodule

# Ask for user input
read -p "Enter your GitHub username: " github_username
read -p "Enter the name for the new GitHub repository: " github_repo
read -p "Enter the name for the submodule folder: " submodule_folder

# Create a new GitHub repository
gh repo create $github_repo --public

# Clone the new repository
git clone https://github.com/$github_username/$github_repo.git

# Create a new folder and navigate into it
cd $submodule_folder

# Initialize a new Git repository
git init

# Add a README file or other initial content
echo "# $submodule_folder" > README.md
git add README.md
git commit -m "Initial commit"

# Push to the new repository
git remote add origin https://github.com/$github_username/$github_repo.git
git push -u origin main

# Go back to the main repository
cd ..

# Add the new repository as a submodule
git submodule add https://github.com/$github_username/$github_repo.git $submodule_folder

# Add and commit changes in the main repository
git add .
git commit -m "Add $submodule_folder as submodule"
git push origin main  # or your branch name
