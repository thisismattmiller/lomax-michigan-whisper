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

    vtt_file = f'/Volumes/NextGlum/lc-lomax/best_vtt_alan-lomax-in-michigan/{i["shelf_id"]}.vtt'

    # print(vtt_file)
    caption_file = webvtt.read(vtt_file)

    
    non_bracket = 0    
    all_captions = ''
    for caption in caption_file:
        if '[' not in caption.text:
            non_bracket+=1

        all_captions = all_captions + caption.text + '\n'
        # print(caption)

    non_eng = False
    for x in i['language']:
        if x != 'english':
            non_eng=x

    if non_eng:
        # if 'translation' in i:
        #     print('skip',i["shelf_id"], 'aready done')
        #     continue

        print(i['language'],non_eng)

        messages = [
            {"role": "system", "content": f"You are a helpful assistant that translates song lyrics from {non_eng.title()} to English."},
            {"role": "user", "content": f'Translate each line of the following lyrics from {non_eng.title()} to English language, return as a JSON response with a top level array of each line in English, make no other changes to the text except translation, the response must be in English:\n "{"".join(all_captions)}"'}
          ]

        print(messages)

        response = client.chat.completions.create(
          model="gpt-4o",
          response_format={ "type": "json_object" },
          temperature = 0,
          messages=messages
        )
        print(response.choices[0].message.content)
        try:
            transdata = json.loads(response.choices[0].message.content)
        except:
            print("Not valid JSON :(")

        
        if 'lyrics' in transdata:
            i['translation'] = transdata['lyrics']

            json.dump(data,open('metadata_alan-lomax-in-michigan.json','w'),indent=2)

        else:
            print("Unexpected format", response.choices[0].message.content)
            break


    
 


# response = client.chat.completions.create(
#   model="gpt-4o",
#   response_format={ "type": "json_object" },
#   temperature = 0,
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant translating designed to output JSON."},
#     {"role": "user", "content": "Who won the world series in 2020?"}
#   ]
# )
# print(response.choices[0].message.content)