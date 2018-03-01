from django.views.generic.base import TemplateView


class WebsiteView(TemplateView):
    template_engine = 'jinja2'


class IndexView(WebsiteView):
    template_name = 'index.html'


class ContactUsView(WebsiteView):
    template_name = 'contactus.html'


class ForumView(WebsiteView):
    template_name = 'forum.html'


class LegalView(WebsiteView):
    template_name = 'legal.html'


class PrivacyPolicyView(WebsiteView):
    template_name = 'privacypolicy.html'


class SearchView(WebsiteView):
    template_name = 'search.html'


class AboutView(WebsiteView):
    template_name = 'about.html'
