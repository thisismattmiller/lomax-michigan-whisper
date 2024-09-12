import openai
import os
import glob




openai.api_key = os.getenv("OPENAI_API_KEY")


for file in glob.glob('/Volumes/NextGlum/lc-lomax/converted_second_pass/*.wav'):

	print(file)
	filename = file.split('/')[-1]
	filename = filename + '.vtt'

	f = open(file, "rb")
	transcript = openai.Audio.transcribe("whisper-1", f, temperature=0, verbose=True, response_format="vtt", compression_ratio_threshold=1.0)	


	with open(f"openai_transcripts/{filename}",'w') as out:
		out.write(transcript)
