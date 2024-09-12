import json
import glob
import os
import webvtt


iso={
	'fi' : 'finnish',
	'sr' : 'serbian',
	'en' : 'english',
	'ro' : 'romanian',
	'pl' : 'polish',
	'hu' : 'hungarian',
	'fr' : 'french',
	'lt' : 'lithuanian',
	'ru' : 'russian',
	'de' : 'german',
	'it' : 'italian',
	'hr': 'croatian'
}

data = json.load(open('metadata_alan-lomax-in-michigan.json'))


for rec in data:

	id = rec['aka'][0].split('/')[-2]
	file = f"/Volumes/NextGlum/lc-lomax/best_vtt_alan-lomax-in-michigan/{id}.vtt"

	if os.path.isfile(file) == True:

		
		html = "<html><head>"

		lang = iso[rec['language_iso']]
		
		
		html = html + "</head><body>"

		html = html + f"<h1>{rec['title']}</h1>\n<ul>\n"

		for location in rec['location']:
			html = html + f'<div data-pagefind-filter="location">{location.title()}</div>\n'

		subjects = []

		for subject in rec['subject']:
			subjects.append(subject.title())
			# html = html + f'<div data-pagefind-filter="subject">{subject}</div>\n'
		
		if 'generateSubjectsRecon' in rec:
			for subject in rec['generateSubjectsRecon']:
				if subject != False:
					# html = html + f'<div data-pagefind-filter="subject">{subject}</div>\n'
					subjects.append(subject.title())


		for subject in list(set(subjects)):
			if '19' not in subject and '20' not in subject:
				html = html + f'<div data-pagefind-filter="subject">{subject}</div>\n'


		html = html + f'<div data-pagefind-filter="language">{lang}</div>\n'


		caption_file = webvtt.read(file)

		for caption in caption_file:
			html = html + f"<li>{caption.text.strip()}</li>\n"

		html = html + "<hr/>"

		if 'translation' in rec:
			for line in rec['translation']:
				print(line)
				html = html + f"<li>{line}</li>\n"


		html = html + "</ul>\n</body>\n</html>"		

		with open(f'search_pages/pages/{id}.html','w') as outfile:

			outfile.write(html)


		# 

		# text = {}
		# total_lines = 0


		# 

		# 	caption.text = caption.text.replace('♪','')


	else:

		print("Cannot find vtt for ",file)



# for file in glob.glob("/Volumes/NextGlum/lc-lomax/best_vtt_alan-lomax-in-michigan/*.wav.vtt"):


