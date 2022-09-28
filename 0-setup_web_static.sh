#!/usr/bin/env bash

sudo apt -y update
sudo apt -y install nginx

sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
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
sed -i '55i\	}' /etc/nginx/sites-available/default

service nginx restart