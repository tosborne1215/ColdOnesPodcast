import unittest
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from .models import Episode

# note - this code can be run only once. Hack to allow acces to context variables
# See here: https://stackoverflow.com/questions/1941980/how-can-i-access-response-context-when-testing-a-jinja2-powered-django-view
from jinja2 import Template as Jinja2Template
from django.test import signals
ORIGINAL_JINJA2_RENDERER = Jinja2Template.render


def instrumented_render(template_object, *args, **kwargs):
    context = dict(*args, **kwargs)
    # More context hacks. The data is loaded after the jinja_config is loaded so when jinja2_config
    # sets the context, it doesnt have any data. Since this is before the render of the tempalate
    # it works nicely.
    signals.template_rendered.send(
        sender=template_object,
        template=template_object,
        context=context
    )
    return ORIGINAL_JINJA2_RENDERER(template_object, *args, **kwargs)


Jinja2Template.render = instrumented_render


class PodcastTest(TestCase):
    fixtures = ['test.data.json']

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_i_have_episodes(self):
        self.assertGreater(Episode.objects.count(), 0)

    def test_index_has_latest_episode_context(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['latest'].id, 10)

    def test_index_has_previous_episode_context(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['previous'].id, 9)

    def test_index_has_latest_episode_link(self):
        response = self.client.get(reverse('index'))
        self.assertContains(
            response, """<a class="dropdown-item" href="/podcast/episode/10">Latest <span class="badge badge-secondary">New</span></a>""", 1, 200)

    def test_index_has_previous_episode_link(self):
        response = self.client.get(reverse('index'))
        self.assertContains(
            response, """<a class="dropdown-item" href="/podcast/episode/9">Previous</a>""", 1, 200)

    def test_episode_list_page(self):
        response = self.client.get(reverse('podcast:episodes'))

        episodes = Episode.objects.all()

        self.assertGreater(Episode.objects.count(), 0)
        for episode in episodes:
            self.assertIn(episode, response.context['object_list'])

    # Order should be by published dates
    def test_episode_list_page_order_is_correct(self):
        response = self.client.get(reverse('podcast:episodes'))

        episodes = Episode.objects.order_by('-pub_date')

        self.assertEquals(episodes.count(), len(
            response.context['object_list']))
        for episodeA, episodeB in zip(episodes, response.context['object_list']):
            self.assertEquals(episodeA.id, episodeB.id)


class PodcastFeedTest(TestCase):
    fixtures = ['test.data.json']

    def setUp(self):
        self.client = Client()

    def test_rss_exists(self):
        response = self.client.get(reverse('podcastfeed'))
        response2 = self.client.get(reverse('podcast:feed'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response2.status_code, 200)

    def test_rss_feed_is_valid(self):
        pass

    def test_rss_feed_contains_episode(self):
        episode = Episode.objects.all()[:1][0]

        response = self.client.get(reverse('podcast:feed'))
        self.assertContains(response, episode.title, 1, 200)

    def test_rss_feed_episode_has_all_details(self):
        episode = Episode.objects.all()[:1][0]

        response = self.client.get(reverse('podcast:feed'))
        self.assertContains(response, episode.title, 1, 200)
        # 3 due to the description, itunes:description, googeplay:description
        self.assertContains(response, episode.description, 3, 200)

    def test_rss_feed_contains_all_episodes(self):
        response = self.client.get(reverse('podcast:feed'))
        episodes = Episode.objects.all()

        self.assertGreater(Episode.objects.count(), 0)
        for episode in episodes:
            self.assertContains(response, episode.title, 1, 200)

    # TODO: I'm not sure how to effectively test this
    def test_rss_feed_episode_order(self):
        pass


class EpisodeUploadTest(TestCase):

    def test_upload(self):
        pass

    def test_download(self):
        pass
