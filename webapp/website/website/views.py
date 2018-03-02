from django.views.generic.base import TemplateView
from podcast.episode_context_mixin import EpisodeContextMixin


class WebsiteView(TemplateView, EpisodeContextMixin):
    template_engine = 'jinja2'


class IndexView(WebsiteView, EpisodeContextMixin):
    template_name = 'index.html'


class ContactUsView(WebsiteView, EpisodeContextMixin):
    template_name = 'contactus.html'


class ForumView(WebsiteView, EpisodeContextMixin):
    template_name = 'forum.html'


class LegalView(WebsiteView, EpisodeContextMixin):
    template_name = 'legal.html'


class PrivacyPolicyView(WebsiteView, EpisodeContextMixin):
    template_name = 'privacypolicy.html'


class SearchView(WebsiteView, EpisodeContextMixin):
    template_name = 'search.html'


class AboutView(WebsiteView, EpisodeContextMixin):
    template_name = 'about.html'
