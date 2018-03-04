from django.views.generic.base import ContextMixin
from .models import Episode


class EpisodeContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(EpisodeContextMixin, self).get_context_data(**kwargs)
        
        if Episode.objects.count() >= 2:
            last2Episodes = Episode.objects.order_by('-pub_date')[:2]
            context['latest'] = last2Episodes[0]
            context['previous'] = last2Episodes[1]
            context['show_episodes'] = True
        else:
            context['show_episodes'] = False
        return context
