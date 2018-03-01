#!/bin/bash

`sudo docker-compose -f docker-compose.dev.yml exec webapp /usr/bin/touch /etc/uwsgi/django-uwsgi.ini`
