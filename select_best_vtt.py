import json
import os.path
import shutil


data = json.load(open('metadata_alan-lomax-in-michigan.json'))


for rec in data:

	id = rec['aka'][0].split('/')[-2]

	if os.path.isfile(f"/Volumes/NextGlum/lc-lomax/openai_vtt_alan-lomax-in-michigan/{id}.wav.vtt") == True:
		shutil.copy(f"/Volumes/NextGlum/lc-lomax/openai_vtt_alan-lomax-in-michigan/{id}.wav.vtt",f"/Volumes/NextGlum/lc-lomax/best_vtt_alan-lomax-in-michigan/{id}.wav.vtt")
	elif os.path.isfile(f"/Volumes/NextGlum/lc-lomax/medium_vtt_alan-lomax-in-michigan/{id}.wav.vtt") == True:
		shutil.copy(f"/Volumes/NextGlum/lc-lomax/medium_vtt_alan-lomax-in-michigan/{id}.wav.vtt",f"/Volumes/NextGlum/lc-lomax/best_vtt_alan-lomax-in-michigan/{id}.wav.vtt")
	elif os.path.isfile(f"/Volumes/NextGlum/lc-lomax/large_vtt_alan-lomax-in-michigan/{id}.wav.vtt") == True:
		shutil.copy(f"/Volumes/NextGlum/lc-lomax/large_vtt_alan-lomax-in-michigan/{id}.wav.vtt",f"/Volumes/NextGlum/lc-lomax/best_vtt_alan-lomax-in-michigan/{id}.wav.vtt")

	else:

		print("Error on:",id)
