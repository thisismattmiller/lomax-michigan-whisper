import json
import os.path
import subprocess


data = json.load(open('metadata_alan-lomax-in-michigan.json'))

langs={}
iso={
	'finnish': 'fi', 
	'serbian': 'sr', 
	'english': 'english', 
	'romanian': 'ro', 
	'polish': 'pl', 
	'hungarian': 'hu', 
	'french': 'fr', 
	'lithuanian': 'lt', 
	'russian': 'ru', 
	'german': 'de', 
	'italian': 'it', 
	'croatian': 'hr'
}

for rec in data:

	print(rec['language'])
	only_eng = True
	for l in rec['language']:
		if l not in langs:
			if l != 'english' and l in iso:
				rec['language_iso'] = iso[l]
			else:
				rec['language_iso'] = 'en'


json.dump(data,open('metadata_alan-lomax-in-michigan.json','w'),indent=2)



