import json
import os.path
import subprocess
import shutil
import webvtt # pip install webvtt-py
import glob
# import openai


data = json.load(open('metadata_alan-lomax-in-michigan.json'))


models = ['ggml-large-v3','ggml-large-v2','ggml-large-v1','ggml-medium']



for m in models:

	count = 0
	for rec in data:

		count=count+1
		print("Doing",m,count,'/',len(data))

		id = rec['aka'][0].split('/')[-2]
		iso = rec['language_iso']
		
		# do we have it for the this model ?
		if os.path.isfile(f"/Volumes/NextGlum/lc-lomax/{m}_vtt_alan-lomax-in-michigan/{id}.wav.vtt") == True:
			continue

		print("Running: ", f"/Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan_converted/{id}.wav", f" For {m}")
		cmd_str = f"/Users/m/git/whisper.cpp/main -m /Users/m/git/whisper.cpp/models/{m}.bin --output-vtt -l {iso} -f /Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan_converted/{id}.wav"
		print(cmd_str)
		subprocess.run(cmd_str, shell=True)
		shutil.move(f"/Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan_converted/{id}.wav.vtt", f"/Volumes/NextGlum/lc-lomax/{m}_vtt_alan-lomax-in-michigan/{id}.wav.vtt")

