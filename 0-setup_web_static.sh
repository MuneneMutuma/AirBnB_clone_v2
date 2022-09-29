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

sudo chown "$USER":"$USER" -R /data/

sed -i '53i\	location /hbnb_static {' /etc/nginx/sites-available/default
sed -i '54i\		alias /data/web_static/current/;' /etc/nginx/sites-available/default
sed -i '55i\		index index.html index.htm;' /etc/nginx/sites-available/default
sed -i '56i\	}' /etc/nginx/sites-available/default

service nginx restart
