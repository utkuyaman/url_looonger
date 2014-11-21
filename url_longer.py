
links = [
	"http://bit.ly/url_loonger",
]

import urllib
import urllib2
import datetime

print str(datetime.datetime.now())
for link in links:
	try:
		resp = urllib.urlopen(link)
		if resp.getcode() is 200:
			print resp.url
	except:
		print 'error: ', link

print str(datetime.datetime.now())

for link in links:
	try:
		request = urllib2.Request(link)
		request.get_method = lambda : 'HEAD'
		response = urllib2.urlopen(request)
		print response.geturl()
	except:
		print 'error: ', link

print str(datetime.datetime.now())
