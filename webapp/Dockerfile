FROM python:3.6
ARG DJANGO_PROJECT_NAME
# Add code
ADD ./${DJANGO_PROJECT_NAME} /srv/${DJANGO_PROJECT_NAME}

# Install application requirements
ADD ./config/requirements.txt /srv/${DJANGO_PROJECT_NAME}/
RUN pip install -r /srv/${DJANGO_PROJECT_NAME}/requirements.txt

# Add start script
ADD ./config/start.sh /

# Add uWSGI config
ADD ./config/django-uwsgi.ini /etc/uwsgi/django-uwsgi.ini

# Add database check script
ADD ./config/database-check.py /srv/config/database-check.py

# Create django user, will own the Django app
RUN adduser --no-create-home --disabled-login --group --system django
RUN chown -R django:django /srv/${DJANGO_PROJECT_NAME}

# Execute start script
CMD ["./start.sh"]
