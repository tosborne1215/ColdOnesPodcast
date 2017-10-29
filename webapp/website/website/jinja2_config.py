from __future__ import absolute_import  # Python 2 only

from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment, PackageLoader, select_autoescape


def environment(**options):
    env = Environment(
        loader=PackageLoader('website', 'jinja2'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env

