import os
import json
import requests
import time
import string





data = json.load(open('metadata_alan-lomax-in-michigan.json'))
all_subjects={}
for i in data:


    if 'generateSubjectsRecon' not in i:
        continue

    for s in i['generateSubjectsRecon']:

        if i['generateSubjectsRecon'][s] == False:

            if s not in all_subjects:
                all_subjects[s] = 0

            all_subjects[s]=all_subjects[s]+1

print(json.dumps(all_subjects,indent=2))



    # i['generateSubjectsRecon'] = generateSubjectsRecon
    # json.dump(data,open('metadata_alan-lomax-in-michigan.json','w'),indent=2)
    




    # elif 'headings' in subjects:
    #     i['generateSubjects'] = subjects['headings']

    #     json.dump(data,open('metadata_alan-lomax-in-michigan.json','w'),indent=2)




        


