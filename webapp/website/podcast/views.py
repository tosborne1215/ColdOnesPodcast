from django.views import generic
from .models import Episode

# Create your views here.


class EpisodesView(generic.ListView):
    template_name = 'podcast/episodes.html'
    model = Episode

    def get_queryset(self):
        return Episode.objects.all()


class EpisodeView(generic.DetailView):
    template_name = 'podcast/episode.html'
    model = Episode
    context_object_name = 'episode'
