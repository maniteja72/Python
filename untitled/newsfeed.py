import feedparser
import notify2
import os
import time
def parseFeed():
    f = feedparser.parse('http://feeds.feedburner.com/ndtvnews-world-news')
    ICON_PATH = os.getcwd() + "/icon.ico"
    notify2.init("news nofiyication")

    for newsitem in f('items'):
        n = notify2.notification(newsitem['title'],
                                 newsitem['summary'],
                                 icon = ICON_PATH
        )
        n.set_urgency(notify2.URGENCY_CRITICAL)
        n.show()
        n.set_timeout(5000)
        time.sleep(900)
        if _name_ == '_main_':
        parseFeed()