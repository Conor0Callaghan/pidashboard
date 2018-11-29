#!/usr/bin/python3

import feedparser

# https://github.com/kurtmckee/feedparser/issues/30
def feedparser_parse(uri):
  try:
    return feedparser.parse(uri)
  except TypeError:
    if 'drv_libxml2' in feedparser.PREFERRED_XML_PARSERS:
      feedparser.PREFERRED_XML_PARSERS.remove('drv_libxml2')
      return feedparser.parse(uri)
    else:
      raise


def retrieveHeadlines():

  uri = 'http://feeds.bbci.co.uk/news/rss.xml'

  data = feedparser_parse(uri)

  headlines = (data.entries[0].title + '<br>' + data.entries[1].title + '<br>' +  data.entries[2].title + '<br>' + data.entries[3].title)

  return headlines
