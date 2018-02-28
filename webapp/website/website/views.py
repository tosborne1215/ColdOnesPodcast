from django.shortcuts import render
from podcast.models import Episode
from django.views.generic.base import TemplateView


class WebsiteView(TemplateView):
    template_engine = 'jinja2'

    def get_context_data(self, **kwargs):
        context = super(WebsiteView, self).get_context_data(**kwargs)
        if Episode.objects.count() >= 2:

            last2Episodes = Episode.objects.order_by('-pub_date')[:2]
            context['latest'] = last2Episodes[0].id
            context['previous'] = last2Episodes[1].id
            context['show_episodes'] = True
        else:
            context['show_episodes'] = False
        return context


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


def index(request):
    response = request

    return render(response, 'index.html', context, status=200, using='jinja2')


def contactus(request):
    response = request
    context = dict()
    return render(response, 'contactus.html', context, status=200, using='jinja2')


def forum(request):
    response = request
    context = dict()
    return render(response, 'forum.html', context, status=200, using='jinja2')


def legal(request):
    response = request
    context = dict()
    return render(response, 'legal.html', context, status=200, using='jinja2')


def privacypolicy(request):
    response = request
    context = dict()
    return render(response, 'privacypolicy.html', context, status=200, using='jinja2')


def search(request):
    response = request
    context = dict()
    return render(response, 'search.html', context, status=200, using='jinja2')


def about(request):
    response = request
    context = dict()
    return render(response, 'about.html', context, status=200, using='jinja2')
