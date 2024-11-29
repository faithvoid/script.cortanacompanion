#!/bin/bash

# Ensure the script runs with superuser privileges
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root. Please use sudo."
    exit 1
fi

# Function to check if a package is installed
is_installed() {
    dpkg -l | grep -qw "$1"
}

# Install required packages
echo "Checking for required packages..."
packages=(python3 python3-rpi.gpio python3-luma.oled)
for pkg in "${packages[@]}"; do
    if is_installed "$pkg"; then
        echo "$pkg is already installed. Skipping."
    else
        echo "$pkg is not installed. Installing..."
        apt install -y "$pkg"
    fi
done

# Download required files
wget https://raw.githubusercontent.com/faithvoid/script.cortanacompanion/refs/heads/main/release/CortanaCompanion.py
wget https://raw.githubusercontent.com/faithvoid/script.cortanacompanion/refs/heads/main/release/CortanaDisplay.service
mkdir /opt/CortanaCompanion

# Copy service files to systemd directory
cp CortanaCompanion.service /etc/systemd/system/
cp CortanaCompanion.py /opt/CortanaCompanion

# Enable and start services
systemctl enable CortanaCompanion.service
systemctl start CortanaCompanion.service 

# Remove copied files
rm CortanaCompanion.py
rm CortanaCompanion.service

# Inform the user that the setup is complete
echo "Cortana Companion setup complete. Services have been started and enabled."
