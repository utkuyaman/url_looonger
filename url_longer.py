import os
import sys
import urllib2
import re


def longen(link):
	try:
		request = urllib2.Request(link)
		request.get_method = lambda : 'HEAD'
		response = urllib2.urlopen(request)
		print(response.geturl())
	except:
		print('error: ', link)

# check if link is supplied by stdin
if os.fstat(sys.stdin.fileno()).st_size > 0:
	for line in sys.stdin:
		longen(line)
elif len(sys.argv) > 1:
	links = []

	val = sys.argv[1]

	# check if the argument is a file
	if os.path.isfile(val):
		with open(val) as f:
			links = f.readlines()
	else:
		links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', val)

	if len(links) == 0:
		print('error: where are the links?')
	else:
		# parse links
		for link in links:
			longen(link)
else:
	print('error: where are the links?')
