#! /bin/bash
envsubst $(compgen -v | grep NGINX* | sed 's/NGINX/$NGINX/' | tr "\n" ",") < nginx.tmpl > /etc/nginx/nginx.conf

nginx -g "daemon off;"
