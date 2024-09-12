
import json
from pathlib import Path

data = json.load(open('metadata_alan-lomax-in-michigan.json'))


models = ['ggml-large-v3','ggml-large-v2','ggml-large-v1','ggml-medium']


final_data = {}





for rec in data:
	id = rec['aka'][0].split('/')[-2]
	final_data[id] = {'id':id,'lang':rec['language_iso']}
	for m in models:
		final_data[id][m] = ''
		p = f"/Volumes/NextGlum/lc-lomax/{m}_vtt_alan-lomax-in-michigan/{id}.wav.vtt"
		


		if Path(p).is_file():

			final_data[id]
			contents = Path(p).read_text()

			final_data[id][m] = contents


for rec in final_data:

	# look for which one has the least repeated phases
	final_data[rec]['dupe_score'] = {}
	final_data[rec]['line_count'] = {}
	final_data[rec]['unique_count'] = {}

	final_data[rec]['dupe_lines'] = {}

	for m in models:
		print(rec,m)
		total_lines = 0
		for l in final_data[rec][m].split("\n"):
			if l.strip() != '':
				if '-->' not in l and 'WEBVTT' not in l:
					
					total_lines+=1

		dupe_lines = 0
		previousLines = []
		for line in final_data[rec][m].split("\n"):

			if line.startswith('WEBVTT') == False and line.strip() != '' and line.startswith('00:') == False:
				if line in previousLines:
					# print(previousLines)
					# print(dupe_lines)
					dupe_lines=dupe_lines+1
				else:
					previousLines.append(line)


		dupe_score = dupe_lines/total_lines*100
		final_data[rec]['dupe_score'][m] = dupe_score
		final_data[rec]['line_count'][m] = total_lines
		final_data[rec]['dupe_lines'][m] = dupe_lines


		final_data[rec]['unique_count'][m] = len(previousLines)






json.dump(final_data,open('qa_model.json','w'))


