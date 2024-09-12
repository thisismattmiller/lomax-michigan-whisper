import requests
import json
import time


data = []
for page in range(1,19):

	req = requests.get(f'https://www.loc.gov/collections/alan-lomax-in-michigan/?fa=original-format:sound+recording&sp={page}&fo=json')
	d = req.json()
	r = d['content']['results']
	data = data + d['content']['results']
	print(page)
	time.sleep(5)

json.dump(data,open('metadata_alan-lomax-in-michigan.json','w'),indent=2)







data = []
for page in range(1,29):

	req = requests.get(f'https://www.loc.gov/collections/john-and-ruby-lomax/?fa=original-format:sound+recording&sp={page}&fo=json')
	d = req.json()
	r = d['content']['results']
	data = data + d['content']['results']
	print(page)
	time.sleep(5)

json.dump(data,open('metadata_john-and-ruby-lomax.json','w'),indent=2)




