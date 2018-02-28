from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404
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

def index(request):
    return "Stuff2"

def latest(request):
    response = request
    context = dict()
    return render(response,'podcast/episode.html',context,status=200,using='jinja2')

def previous(request):
    response = request
    context = dict()
    return render(response,'podcast/episode.html',context,status=200,using='jinja2')

def episodes(request):
    response = request
    context = dict()
    return render(response,'podcast/episode.html',context,status=200,using='jinja2')

def episode(request, id):
    response = request
    context = dict()
    return render(response,'podcast/episode.html',context,status=200,using='jinja2')