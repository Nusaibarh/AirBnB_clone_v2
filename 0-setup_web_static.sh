#!/bin/bash

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    apt-get update
    apt-get -y install nginx
fi

# Create necessary folders if they don't exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "This is a test" > /data/web_static/releases/test/index.html

# Create a symbolic link
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
sed -i '/location \/hbnb_static {/ a \        alias /data/web_static/current/;' "$config_file"

# Restart Nginx
service nginx restart

exit 0
