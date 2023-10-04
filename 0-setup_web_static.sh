#!/usr/bin/env bash

# Script Description:
# This Bash script automates the setup of an Nginx web server and directory structure for serving web content. It performs the following tasks:
# 1. Checks if Nginx is installed and installs it if not.
# 2. Creates directories to organize web application files.
# 3. Generates a simple "Welcome" page in the test directory.
# 4. Sets up a symbolic link to manage the current version of the web application.
# 5. Configures Nginx to serve web content and handle specific URL paths.
# 6. Restarts the Nginx service to apply the configuration.

if ! command -v nginx &> /dev/null; then
    # Check if Nginx is installed; if not, update package list and install Nginx.
    sudo apt-get update
    sudo apt-get -y install nginx 
fi

# Directory structure for organizing web content
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a simple "Welcome" page
echo "Welcome" > /data/web_static/releases/test/index.html

# Set up a symbolic link for managing the current version
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Ensure proper ownership for web server access
sudo chown -R ubuntu:ubuntu /data/

# Nginx server configuration
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index yasin.html index.html index.nginx-debian.html;
    add_header X-Served-By $(hostname);
    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /notfound.html;
    location = /notfound {
        root /var/www/html;
        internal;
    }
}" | sudo tee /etc/nginx/sites-available/default

# Restart Nginx to apply the configuration
sudo service nginx restart

