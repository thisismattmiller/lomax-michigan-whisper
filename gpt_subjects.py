from openai import OpenAI
import os
import json
import webvtt

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


data = json.load(open('metadata_alan-lomax-in-michigan.json'))

for i in data:

    if 'generateSubjects' in i:
        continue

    vtt_file = f'/Volumes/NextGlum/lc-lomax/best_vtt_alan-lomax-in-michigan/{i["shelf_id"]}.vtt'

    print(vtt_file)
    caption_file = webvtt.read(vtt_file)

    
    non_bracket = 0    
    all_captions = ''
    for caption in caption_file:
        if '[' not in caption.text:
            non_bracket+=1

        all_captions = all_captions + caption.text + '\n'
        print(caption)



    year = i['date'].split("-")[0]
    if len(i["language"]) == 1:
        lang = i["language"][0]
    else:
        lang = ''

    messages = [
        {"role": "system", "content": f"You are a helpful assistant generating Library of Congress Subject Headings (LCSH) for songs based on their lyrics."},
        {"role": "user", "content": f'Generate the most relevant five Library of Congress Subject Headings (LCSH) for for this {year} {lang} folk song as a JSON array based on the lyrics: {all_captions}'}
      ]

    print(messages)

    response = client.chat.completions.create(
      model="gpt-4o",
      response_format={ "type": "json_object" },
      temperature = 0,
      messages=messages
    )
    print(response.choices[0].message.content)

    if 'Insufficient information' in response.choices[0].message.content:
        continue


    try:
        subjects = json.loads(response.choices[0].message.content)
    except:
        print("Not valid JSON :(")

    
    if 'LCSH' in subjects:
        i['generateSubjects'] = subjects['LCSH']

        json.dump(data,open('metadata_alan-lomax-in-michigan.json','w'),indent=2)

    elif 'subjects' in subjects:
        i['generateSubjects'] = subjects['subjects']

        json.dump(data,open('metadata_alan-lomax-in-michigan.json','w'),indent=2)

    elif 'subject_headings' in subjects:
        i['generateSubjects'] = subjects['subject_headings']

        json.dump(data,open('metadata_alan-lomax-in-michigan.json','w'),indent=2)

    elif 'headings' in subjects:
        i['generateSubjects'] = subjects['headings']

        json.dump(data,open('metadata_alan-lomax-in-michigan.json','w'),indent=2)




        

    else:
        print("Unexpected format", response.choices[0].message.content)
        break


    
 


