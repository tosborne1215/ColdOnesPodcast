from django.views import generic
from .models import Episode
from .episode_context_mixin import EpisodeContextMixin


class EpisodesView(generic.ListView, EpisodeContextMixin):
    template_name = 'podcast/episodes.html'
    model = Episode

    def get_queryset(self):
        return Episode.objects.order_by('-pub_date')


class EpisodeView(generic.DetailView, EpisodeContextMixin):
    template_name = 'podcast/episode.html'
    model = Episode
    context_object_name = 'episode'
