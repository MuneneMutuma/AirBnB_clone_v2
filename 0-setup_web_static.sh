#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

sudo apt -y update
sudo apt -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html

echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" | sudo tee -a /data/web_static/releases/test/index.html


sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown ubuntu -R /data/
sudo chgrp ubuntu -R /data/

printf %s "srever {
	listen 80 default_server;
	listen [::]:80 default_server;

	add_header X-Served-By $HOSTNAME;
	root /var/www/html;
	index index.html index.htm;

	location /hbnb_static {
		alias /data/web_static/current;
		index index.html index.htm;
	}
}" > /etc/nginx/sites-available/default

service nginx restart

service nginx restart
