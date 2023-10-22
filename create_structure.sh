#!/bin/bash

# Function to create directories and files
create_structure() {
    # Create directories
    mkdir -p memory-alert-system/api
    mkdir -p memory-alert-system/monitor

    # Change to the project directory
    cd memory-alert-system

    # Create files inside api directory
    touch api/app.py
    echo "flask" >> api/requirements.txt  # adding example dependency

    # Create files inside monitor directory
    touch monitor/monitor.py
    echo "psutil" >> monitor/requirements.txt  # adding example dependency
    echo "requests" >> monitor/requirements.txt  # adding another example dependency

    # Create .gitignore, README.md, and LICENSE in the root of the project directory
    touch .gitignore
    touch README.md
    touch LICENSE
}

# Create the project structure
create_structure

# Print the structure
echo "Project structure created:"
tree memory-alert-system  # 'tree' command should be installed to visualize the folder structure
