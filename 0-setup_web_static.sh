#!/usr/bin/env bash
# script that configures servers
apt-get update
dpkg -l | grep -qw nginx || apt-get -y install nginx
mkdir -p data/web_static/shared
mkdir -p data/web_static/releases/test
echo "hello" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server;/a location /hbnb_static {alias /data/web_static/current/}' /etc/nginx/sites-available/default
service nginx restart
exit 0
