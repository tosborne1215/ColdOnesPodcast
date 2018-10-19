from django.contrib.syndication.views import Feed
from django.utils import feedgenerator
from .models import Episode


class iTunesFeed(feedgenerator.Rss201rev2Feed):
    def rss_attributes(self):
        attrs = super(iTunesFeed, self).root_attributes()
        attrs['xmlns:itunes'] = 'http://www.itunes.com/dtds/podcast-1.0.dtd'
        attrs['xmlns:googleplay'] = "http://www.google.com/schemas/play-podcasts/1.0/play-podcasts.xsd"
        attrs['xmlns:atom'] = "http://www.w3.org/2005/Atom"
        attrs['version'] = "2.0"
        return attrs

    def add_root_elements(self, handler):
        super(iTunesFeed, self).add_root_elements(handler)

        handler.startElement("image", {})
        handler.addQuickElement("url", self.feed['image'])
        handler.addQuickElement("title", self.feed['title'])
        handler.addQuickElement("link", self.feed['feed_url'])
        handler.addQuickElement("googleplay:image", '', {
                                'href': 'https://episodes.nyc3.digitaloceanspaces.com/ColdOne/static-assets/mainimage.jpg'})
        handler.addQuickElement("itunes:image", '', {
                                'href': 'https://episodes.nyc3.digitaloceanspaces.com/ColdOne/static-assets/mainimage.jpg'})
        handler.endElement("image")

        handler.addQuickElement('itunes:explicit', 'yes')
        handler.addQuickElement("googleplay:explicit", 'yes')
        handler.addQuickElement('itunes:image', '', {
                                'href': 'https://episodes.nyc3.digitaloceanspaces.com/ColdOne/static-assets/mainimage.jpg'})
        handler.addQuickElement('itunes:category', '', {'text': 'Comedy'})
        handler.addQuickElement('googleplay:category', '', {'text': 'Comedy'})

        if self.feed['author_name'] is not None:
            handler.addQuickElement(
                "googleplay:author", self.feed['author_name'])
            handler.addQuickElement("itunes:author", self.feed['author_name'])
            handler.startElement("itunes:owner", {})
            handler.addQuickElement("itunes:name", self.feed['author_name'])
            if self.feed["author_email"] is not None:
                handler.addQuickElement(
                    "itunes:email", self.feed["author_email"])

            handler.endElement("itunes:owner")

        if self.feed['author_email'] is not None:
            handler.addQuickElement(
                "googleplay:email", self.feed['author_email'])
            handler.addQuickElement("author", self.feed['author_email'])

        if self.feed['description'] is not None:
            handler.addQuickElement(
                "googleplay:description", self.feed['description'])
            handler.addQuickElement("itunes:summary", self.feed['description'])

    def add_item_elements(self, handler, item):
        super(iTunesFeed, self).add_item_elements(handler, item)

        if item['description'] is not None:
            handler.addQuickElement(
                "googleplay:description", item['description'])
            handler.addQuickElement("itunes:summary", item['description'])

        if item['author_name'] is not None:
            handler.addQuickElement("googleplay:author", item['author_name'])
            handler.addQuickElement("itunes:author", item['author_name'])

        # if item['image'] is not None:
        handler.addQuickElement("googleplay:image", "", {
                                "href": "https://episodes.nyc3.digitaloceanspaces.com/ColdOne/static-assets/mainimage.jpg"})

        handler.addQuickElement('itunes:explicit', 'yes')
        handler.addQuickElement("googleplay:explicit", 'yes')


class PodcastFeed(Feed):
    title = "A Couple Cold Ones"
    file_locations = ""
    link = "/podcast/"
    description = "A dark, wild, and irreverent ride through pop culture and current events."
    feed_type = iTunesFeed
    episode_locations = "https://episodes.nyc3.digitaloceanspaces.com/ColdOne/"
    item_enclosure_mime_type = "audio/mpeg"
    author_email = 'acouplecoldones@gmail.com'
    author_name = 'Shawn Freed, Ryan Shaner'
    image = 'https://episodes.nyc3.digitaloceanspaces.com/ColdOne/static-assets/mainimage.jpg'

    def feed_extra_kwargs(self, obj):
        extra = {}
        extra['image'] = self.image
        return extra

    def items(self):
        return Episode.objects.order_by('-pub_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return self.episode_locations + item.episode_file.url

    def item_enclosure_url(self, item):
        return self.episode_locations + item.episode_file.url

    def item_pubdate(self, item):
        return item.pub_date

    def item_author_name(self, item):
        return self.author_name

    def item_author_email(self, item):
        return self.author_email

    def item_enclosure_length(self, item):
        return 255

    def item_image(self, item):
        return self.image
