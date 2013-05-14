import webapp2
from google.appengine.api import urlfetch
from google.appengine.api import taskqueue
from google.appengine.api import memcache

import logging
import urlparse

from fetch_config import config as fetch_config


class FetchHandler(webapp2.RequestHandler):
    def get(self):
        for cluster_id, cluster_attrs in fetch_config.iteritems():
            taskqueue.add(url='/start_fetch', params={'url': cluster_attrs['url'], 'cluster_id': cluster_id, 'is_list': True})

        self.response.write('start fetching...')

    def post(self):
        url, cluster_id, is_list = self.request.get('url'), self.request.get('cluster_id'), self.request.get('is_list')
        defer_fetch(url, cluster_id, is_list)


def defer_fetch(url, cluster_id, is_list=False):

    logging.info('fetching...%s' % url)

    result = urlfetch.fetch(url)

    if is_list:
        appids = result.content.split('|')
        for appid in appids:
            app_url = 'https://%s.appspot.com/2' % appid
            taskqueue.add(url='/start_fetch', params={'url': app_url, 'cluster_id': cluster_id})
    else:
        appid = urlparse.urlparse(url).netloc.split('.')[0]
        if result.status_code == 503:
            memcache.set(appid, False)
        else:
            memcache.set(appid, True)

app = webapp2.WSGIApplication([
    ('/start_fetch', FetchHandler)
], debug=True)
