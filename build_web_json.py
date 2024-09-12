import json


data = json.load(open('metadata_alan-lomax-in-michigan.json'))


output = {}

for i in data:

	if 'translation' not in i:
		i['translation'] = None
	if 'generateSubjectsRecon' not in i:
		i['generateSubjectsRecon'] = None
	
		


	output[i['shelf_id']] = {
		'id' : i['shelf_id'],
		'title' : i['title'],
		'language_iso' : i['language_iso'],
		'translation' : i['translation'],
		'subjects' : i['generateSubjectsRecon'],
		'language' : i['language'],
		'date' : i['date']



	}


with open('docs/data.json','w') as out:
	json.dump(output,out)

	