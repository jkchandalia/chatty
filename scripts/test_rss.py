# https://github.com/feederco/feeder-api
# Use this for a Google Research Feed


# if I can't get an amazon science feed, I can use this as a quick hack
import urllib.request
fp = urllib.request.urlopen("https://www.amazon.science/blog?p=3")
mybytes = fp.read()
mystr = mybytes.decode("utf8")
fp.close()