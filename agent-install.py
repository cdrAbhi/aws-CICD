#!/bin/bash

# Update package lists
echo "Updating package lists..."
sudo apt update

# Install Ruby
echo "Installing Ruby..."
sudo apt install -y ruby-full

# Install wget
echo "Installing wget..."
sudo apt install -y wget

# Navigate to the home directory
echo "Navigating to the home directory..."
cd /home/ubuntu

# Download the CodeDeploy agent installation script
echo "Downloading the CodeDeploy agent installation script..."
wget https://aws-codedeploy-ap-south-1.s3.ap-south-1.amazonaws.com/latest/install

# Give execute permissions to the installation script
echo "Setting execute permissions on the installation script..."
chmod +x ./install

# Install the CodeDeploy agent
echo "Installing the CodeDeploy agent..."
sudo ./install auto

# Verify the installation
echo "Checking the status of the CodeDeploy agent..."
sudo systemctl status codedeploy-agent

# Start the CodeDeploy agent if it's not running
echo "Starting the CodeDeploy agent if necessary..."
if ! systemctl is-active --quiet codedeploy-agent; then
    sudo systemctl start codedeploy-agent
    echo "CodeDeploy agent started."
else
    echo "CodeDeploy agent is already running."
fi

# Check the status again to confirm it's running
sudo systemctl status codedeploy-agent
