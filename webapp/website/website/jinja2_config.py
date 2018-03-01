from __future__ import absolute_import  # Python 2 only

from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse

from jinja2 import Environment
from podcast.models import Episode


def environment(**options):
    env = Environment(**options)
    global_vars = {
        'static': staticfiles_storage.url,
        'url': reverse,
    }
    env.globals.update(global_vars)
    env.globals.update(get_latest_episode_context())
    return env


def get_latest_episode_context():
    context = dict()
    if Episode.objects.count() >= 2:
        last2Episodes = Episode.objects.order_by('-pub_date')[:2]
        context['latest'] = last2Episodes[0].id
        context['previous'] = last2Episodes[1].id
        context['show_episodes'] = True
    else:
        context['show_episodes'] = False

    return context
