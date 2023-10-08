#!/usr/bin/env bash
# Set up our web servers for the deployment of web_static

sudo apt-get update
sudo apt-get install -y nginx
	
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

sudo printf %s "server {
  listen 80 default_server;
  listen [::]:80 default_server;
  add_header X_Served_By \$hostname;
  root	/var/www/html;
  index index.html index.htm;
  location /hbnb_static {
  	alias /data/web_static/current;
	index index.html index.htm;
}
  location /redirect_me {
  	return 301 http://github.com/soukiitos;
}
  error_page 404 /404.html;
  location /404 {
  	root /var/www/html;
	internal;
}
}" | sudo tee /etc/nginx/sites-available/default > /dev/null

sudo service nginx restart
