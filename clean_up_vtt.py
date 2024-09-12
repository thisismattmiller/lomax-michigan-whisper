import webvtt
import glob


bad_ids=[]
all_lyrics = {}
for file in glob.glob('/Volumes/NextGlum/lc-lomax/best_vtt_alan-lomax-in-michigan/*.vtt'):

	caption_file = webvtt.read(file)

	text = {}
	total_lines = 0


	for caption in caption_file:

		caption.text = caption.text.replace('♪','')

		caption.text  = caption.text.strip()
		print(caption.text)

		total_lines+=1
		if caption.text not in text:
			text[caption.text]=0
			
		text[caption.text]+=1

		if caption.text not in all_lyrics:
			all_lyrics[caption.text]=0

		all_lyrics[caption.text]+=1



	print('----------')
	bad=False
	for line in text:

		if text[line]/total_lines >= 0.75:
			bad=True

	if bad == True:
		print("bad")

		id = file.split('/')[-1].split('.')[0]
		print(id)
		bad_ids.append(id)		

print(len(bad_ids), '/', len(list(glob.glob('/Volumes/NextGlum/lc-lomax/best_vtt_alan-lomax-in-michigan/*.vtt'))))
# print(all_lyrics)
# print(len(all_lyrics))