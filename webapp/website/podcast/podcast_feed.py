from django.contrib.syndication.views import Feed
from django.utils import feedgenerator
from django.urls import reverse
from .models import Episode

class iTunesFeed(feedgenerator.Rss201rev2Feed):
    def rss_attributes(self):
        attrs = super(iTunesFeed, self).rss_attributes()
        attrs['xmlns:itunes'] = 'http://www.itunes.com/dtds/podcast-1.0.dtd'
        return attrs

    def root_attributes(self):
        attrs = super(iTunesFeed, self).root_attributes()
        
        return attrs

    def add_root_elements(self, handler):
        super(iTunesFeed, self).add_root_elements(handler)
        handler.addQuickElement('itunes:explicit','no')
        handler.addQuickElement('itunes:image','',{'href':'https://episodes.nyc3.digitaloceanspaces.com/ColdOne/static-assets/mainimage.jpg'})
        handler.addQuickElement('itunes:category','',{'text':'Comedy'})
        if self.feed['author_name'] is not None:
            handler.startElement("itunes:owner", {})
            handler.addQuickElement("itunes:name", self.feed['author_name'])
            if self.feed["author_email"] is not None:
                handler.addQuickElement("itunes:email", self.feed["author_email"])
            handler.endElement("itunes:owner")
    
    def add_item_elements(self, handler, item):
        super(iTunesFeed, self).add_item_elements(handler, item)
        
        for cat in item['categories']:
            handler.addQuickElement("itunes:category", "", {"term": cat})

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
    
    def items(self):
        return Episode.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
   
    def item_link(self, item):
        return self.episode_locations + item.file_location
   
    def item_enclosure_url(self, item):
        return self.episode_locations + item.file_location

    def item_pubdate(self, item):
        return item.pub_date

