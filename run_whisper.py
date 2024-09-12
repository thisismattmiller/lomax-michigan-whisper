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



# for rec in data:

# 	id = rec['aka'][0].split('/')[-2]
# 	iso = rec['language_iso']
	
# 	# do we have it for the large local whisper?
# 	if os.path.isfile(f"/Volumes/NextGlum/lc-lomax/large-v1_vtt_alan-lomax-in-michigan/{id}.wav.vtt") == True:
# 		continue

# 	print("Running: ", f"/Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan_converted/{id}.wav")
# 	cmd_str = f"/Users/m/git/whisper.cpp/main -m /Users/m/git/whisper.cpp/models/ggml-large.bin --output-vtt -l {iso} -f /Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan_converted/{id}.wav"
# 	subprocess.run(cmd_str, shell=True)
# 	shutil.move(f"/Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan_converted/{id}.wav.vtt", f"/Volumes/NextGlum/lc-lomax/large_vtt_alan-lomax-in-michigan/{id}.wav.vtt")


# todo_medium =[]

# for file in glob.glob("/Volumes/NextGlum/lc-lomax/large_vtt_alan-lomax-in-michigan/*.vtt"):

# 	text = {}
# 	total_lines = 0
	
# 	for caption in webvtt.read(file):
# 		total_lines+=1
# 		if caption.text not in text:
# 			text[caption.text]=0
			
# 		text[caption.text]+=1

# 	bad=False
# 	for line in text:

# 		if text[line]/total_lines >= 0.8:
# 			bad=True

# 	if bad == True:
# 		print("bad")
# 		print(text)
# 		id = file.split('/')[-1].split('.')[0]
# 		print(id)
# 		todo_medium.append(id)

# print("doing ",len(todo_medium))


# for rec in data:

# 	id = rec['aka'][0].split('/')[-2]
# 	if id not in todo_medium:
# 		continue

# 	iso = rec['language_iso']
# 	# do we have it for the large local whisper?
# 	if os.path.isfile(f"/Volumes/NextGlum/lc-lomax/medium_vtt_alan-lomax-in-michigan/{id}.wav.vtt") == True:
# 		continue

# 	print("Running: ", f"/Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan_converted/{id}.wav")
# 	cmd_str = f"/Users/m/git/whisper.cpp/main -m /Users/m/git/whisper.cpp/models/ggml-medium.bin --output-vtt -l {iso} -f /Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan_converted/{id}.wav"
# 	subprocess.run(cmd_str, shell=True)
# 	shutil.move(f"/Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan_converted/{id}.wav.vtt", f"/Volumes/NextGlum/lc-lomax/medium_vtt_alan-lomax-in-michigan/{id}.wav.vtt")


# # /Users/m/git/whisper.cpp/main -m /Users/m/git/whisper.cpp/models/ggml-large.bin --output-vtt -l fi -translate -f /Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan_converted/afc1939007_afs02393b.wav

# todo_openai =[]

# for file in glob.glob("/Volumes/NextGlum/lc-lomax/medium_vtt_alan-lomax-in-michigan/*.vtt"):

# 	text = {}
# 	total_lines = 0
	
# 	for caption in webvtt.read(file):
# 		total_lines+=1
# 		if caption.text not in text:
# 			text[caption.text]=0
			
# 		text[caption.text]+=1

# 	bad=False
# 	for line in text:

# 		if text[line]/total_lines >= 0.8:
# 			bad=True

# 	if bad == True:
# 		print("bad")
# 		print(text)
# 		id = file.split('/')[-1].split('.')[0]
# 		print(id)
# 		todo_openai.append(id)

# print("doing open ai",len(todo_openai))

# openai.api_key = os.getenv("OPENAI_API_KEY")


# for rec in data:

# 	id = rec['aka'][0].split('/')[-2]
# 	if id not in todo_openai:
# 		continue

# 	iso = rec['language_iso']
# 	# do we have it for the opeani whisper?
# 	if os.path.isfile(f"/Volumes/NextGlum/lc-lomax/openai_vtt_alan-lomax-in-michigan/{id}.wav.vtt") == True:
# 		continue


# 	f = open(f"/Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan_converted/{id}.wav", "rb")
# 	transcript = openai.Audio.transcribe("whisper-1", f, temperature=0, verbose=True, response_format="vtt", compression_ratio_threshold=1.0)	


# 	open(f"/Volumes/NextGlum/lc-lomax/openai_vtt_alan-lomax-in-michigan/{id}.wav.vtt",'w').write(transcript)
	

# # run the translation
# for rec in data:

# 	id = rec['aka'][0].split('/')[-2]
# 	iso = rec['language_iso']

# 	if iso != 'en':
# 		if os.path.isfile(f"/Volumes/NextGlum/lc-lomax/translation_vtt_alan-lomax-in-michigan/{id}.wav.vtt") == True:
# 			print("Skipp",id)
# 			continue

# 		print(rec)	
# 		# try the large model first
# 		print("Running: ", f"/Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan_converted/{id}.wav")
# 		cmd_str = f"/Users/m/git/whisper.cpp/main -m /Users/m/git/whisper.cpp/models/ggml-large.bin --output-vtt -l {iso} -tr -f /Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan_converted/{id}.wav"
# 		subprocess.run(cmd_str, shell=True)
# 		shutil.move(f"/Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan_converted/{id}.wav.vtt", f"/Volumes/NextGlum/lc-lomax/translation_vtt_alan-lomax-in-michigan/{id}.wav.vtt")


# 		text = {}
# 		total_lines = 0
		
# 		for caption in webvtt.read(f"/Volumes/NextGlum/lc-lomax/translation_vtt_alan-lomax-in-michigan/{id}.wav.vtt"):
# 			total_lines+=1
# 			if caption.text not in text:
# 				text[caption.text]=0
				
# 			text[caption.text]+=1

# 		bad=False
# 		for line in text:

# 			if text[line]/total_lines >= 0.8:
# 				bad=True

# 		if bad == True:
# 			print("bad large translate")
# 			print(text)
# 			id = file.split('/')[-1].split('.')[0]
# 			print(id)
			
# 			# run it through the medium

# 			print("Running: ", f"/Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan_converted/{id}.wav")
# 			cmd_str = f"/Users/m/git/whisper.cpp/main -m /Users/m/git/whisper.cpp/models/ggml-medium.bin --output-vtt -l {iso} -tr -f /Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan_converted/{id}.wav"
# 			subprocess.run(cmd_str, shell=True)
# 			shutil.move(f"/Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan_converted/{id}.wav.vtt", f"/Volumes/NextGlum/lc-lomax/translation_vtt_alan-lomax-in-michigan/{id}.wav.vtt")




# 			text = {}
# 			total_lines = 0
			
# 			for caption in webvtt.read(f"/Volumes/NextGlum/lc-lomax/translation_vtt_alan-lomax-in-michigan/{id}.wav.vtt"):
# 				total_lines+=1
# 				if caption.text not in text:
# 					text[caption.text]=0
					
# 				text[caption.text]+=1

# 			bad=False
# 			for line in text:

# 				if text[line]/total_lines >= 0.8:
# 					bad=True

# 			if bad == True:
# 				print("bad medium translate")
# 				print(text)
# 				id = file.split('/')[-1].split('.')[0]
# 				print(id)
				
# 				# run it through the api
# 				f = open(f"/Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan/{id}.mp3", "rb")
# 				transcript = openai.Audio.translate("whisper-1", f, temperature=0, verbose=True, response_format="vtt", compression_ratio_threshold=1.0)	


# 				open(f"/Volumes/NextGlum/lc-lomax/translation_vtt_alan-lomax-in-michigan/{id}.wav.vtt",'w').write(transcript)
				


