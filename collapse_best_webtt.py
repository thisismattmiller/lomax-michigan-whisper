
import json
from pathlib import Path
import shutil

data = json.load(open('qa_model.json'))


for i in data:

	# if i != 'afc1939007_afs02476a':
	# 	continue

	path_to_use = f"/Volumes/NextGlum/lc-lomax/{data[i]['use_model']}_vtt_alan-lomax-in-michigan/{i}.wav.vtt"
	output = f'/Volumes/NextGlum/lc-lomax/best_vtt_alan-lomax-in-michigan/{i}.vtt'
	shutil.copyfile(path_to_use, output)


	contents=[]
	with open(output, 'r') as content_file:
		contents = content_file.read().strip().split("\n")

	print('-----')
	print(i, '===', data[i]['use_model'])
	all_lines = []
	a_line = {'time':False,'text':False}
	for line in contents[2:]:
		if a_line['time'] == False and a_line['text'] == False:
			a_line['time'] = line
		elif a_line['time'] != False and a_line['text'] == False:
			a_line['text'] = line
		elif a_line['time'] != False and a_line['text'] != False:
			
			all_lines.append(a_line)

			a_line = {'time':False,'text':False}

	# add the last pair in
	all_lines.append(a_line)


	# print("Before--------------")
	# for l in all_lines:
	# 	print(l['time'], l['text'])	
	# print("--------------------")

	keep_looping = True


	while keep_looping == True:
		keep_looping = False

		i = 0
		remove = []
		while i < len(all_lines):

			current_text = all_lines[i]['text']
			try:
				next_text = all_lines[i+1]['text']
			except IndexError:
				break


			current_text = current_text.lower().strip()
			next_text = next_text.lower().strip()

			if current_text == next_text:

				# print(all_lines[i]['text'], ' === ', all_lines[i+1]['text'])

				current_time_stamp_parts = all_lines[i]['time'].split(' ')
				next_time_stamp_parts = all_lines[i+1]['time'].split(' ')

				modified_time_stamp = " ".join([current_time_stamp_parts[0],'-->', next_time_stamp_parts[2]])

				# print(all_lines[i])
				# print(all_lines[i+1])
				# print(all_lines[i]['time'], 'is now', modified_time_stamp)
				remove.append(i+1)

				all_lines[i]['time'] = modified_time_stamp
				break
				



			i += 1

		for r in remove:
			keep_looping = True
			del all_lines[r]
			break

	# print("after--------------")
	# for l in all_lines:
	# 	print(l['time'], l['text'])	
	# print("--------------------")



	# we are also going to look for some model issues where it adds sign offs into the ending silence

	if len(all_lines) > 3:


		i = len(all_lines) - 3
		remove = []
		while i < len(all_lines):
			
			check_str = all_lines[i]['text'].lower()

			ignore_list = ['amara','vidéo','video','merci','www','adieu', 'thank you', '501','.com','revedere','videót','!','thanks','bf-watch','©','(c)','.pl', 'kiito']
			for il in ignore_list:
				if il in check_str:
					all_lines[i]['text'] = '[silence]'



			i += 1
	

	# and clean up the text a bit
	i=0
	while i < len(all_lines):
		
		all_lines[i]['text'] = all_lines[i]['text'].replace("<i>",'')
		all_lines[i]['text'] = all_lines[i]['text'].replace("</i>",'')


		ignore_list = ['amara','feliratok', '.pl','attila','audiodeskrypcja']
		for il in ignore_list:
			if il in all_lines[i]['text'].lower():
				all_lines[i]['text'] = '[...]'

		

		all_lines[i]['text'] = all_lines[i]['text'].replace("\"",'')
	
		if '♪' in all_lines[i]['text'] and len(all_lines[i]['text']) > 2:
			all_lines[i]['text'] = all_lines[i]['text'].replace('♪','')


		all_lines[i]['text'] = all_lines[i]['text'].strip()


		i += 1



	with open(output,'w') as outwrite:

		outwrite.write('WEBVTT\n')
		outwrite.write('\n')


		for l in all_lines:
			outwrite.write(l['time'] +'\n')
			outwrite.write(l['text'] +'\n')
			outwrite.write('\n')


	print("after--------------")
	for l in all_lines:
		print(l['time'], l['text'])	
	print("--------------------")
	# print(all_lines[-1]['time'], all_lines[-1]['text'])

