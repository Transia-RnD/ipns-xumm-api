#!/bin/bash

# Stop the IPFS service
sudo systemctl stop ipfs

# Disable the IPFS service
sudo systemctl disable ipfs

# Remove the systemd service file
sudo rm -f /etc/systemd/system/ipfs.service

# Reload the systemd daemon to apply changes
sudo systemctl daemon-reload

# Remove the IPFS binary
sudo rm -f /usr/local/bin/ipfs

# Remove the IPFS configuration and data (WARNING: This will delete your IPFS data!)
read -p "Are you sure you want to remove all IPFS data? [y/N] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    ipfs_dir="$HOME/.ipfs"
    if [ -d "$ipfs_dir" ]; then
        rm -rf "$ipfs_dir"
        echo "IPFS data directory removed."
    else
        echo "IPFS data directory not found. It may have been removed already."
    fi
else
    echo "IPFS data directory was not removed."
fi

# Close the ports on UFW that were opened for IPFS
sudo ufw delete allow 4001/tcp
# sudo ufw delete allow 5001/tcp
sudo ufw delete allow 8080/tcp
sudo ufw delete allow 9000/tcp

# Reload UFW to apply the changes
sudo ufw reload

echo "IPFS has been removed from your system."