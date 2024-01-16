#!/bin/bash

# Script to add, commit, and push changes in all submodules

# Display a warning
echo "Warning: This script will add, commit, and push changes in all submodules."

# Ask for user confirmation
read -p "Do you want to continue? (y/n): " answer
if [[ "$answer" != "y" && "$answer" != "Y" ]]; then
    echo "Script aborted."
    exit 1
fi

# Ask for a commit message
read -p "Enter commit message for submodule changes: " commit_message

# Iterate over submodules
git submodule foreach "
    # Add changes
    git add .

    # Commit changes
    git commit -m \"$commit_message\"

    # Push changes
    git push origin master  # or your branch name
"

# Add and commit changes in the main repository
git add .
git commit -m "$commit_message"
git push origin master  # or your branch name
