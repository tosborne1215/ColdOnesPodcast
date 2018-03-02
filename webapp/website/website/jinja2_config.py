from __future__ import absolute_import  # Python 2 only

from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse

from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    global_vars = {
        'static': staticfiles_storage.url,
        'url': reverse,
    }
    env.globals.update(global_vars)
    return env
