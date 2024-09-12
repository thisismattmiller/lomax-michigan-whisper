import os
import json
import requests
import time
import string
import copy



def do_search(term):

    url = 'https://id.loc.gov/authorities/subjects/suggest2/'
    payload = {'q': term}

    req = requests.get(url,params=payload)
    data = req.json()
    found = None
    for hit in data['hits']:

        label = hit['suggestLabel'].split(' (USE')[0]
        if term.translate(str.maketrans('', '', string.punctuation)).lower() == label.translate(str.maketrans('', '', string.punctuation)).lower():
            found = hit
            break

    if found != None:
        return found
    else:
        return False

def do_search_naf(term):

    url = 'https://id.loc.gov/authorities/names/suggest2/'
    payload = {'q': term}

    req = requests.get(url,params=payload)
    data = req.json()
    found = None
    for hit in data['hits']:

        label = hit['suggestLabel'].split(' (USE')[0]
        if term.translate(str.maketrans('', '', string.punctuation)).lower() == label.translate(str.maketrans('', '', string.punctuation)).lower():
            found = hit
            break

    if found != None:
        return found
    else:
        return False



data = json.load(open('metadata_alan-lomax-in-michigan.json'))

for i in data:

    if 'generateSubjects' not in i:
        continue


    if 'generateSubjectsRecon' not in i:
        


        generateSubjectsRecon = {}

        for h in i['generateSubjects']:
            h = h.replace(' -- ','--')
            
            r = do_search(h)


            if r != False:

                generateSubjectsRecon[h] = r

            else:

                if '--' in h:


                    for t in h.split("--"):

                        r = do_search(t)

                        if r != False:
                             generateSubjectsRecon[t] = r
                        else:
                             generateSubjectsRecon[t] = False





                else:
                    generateSubjectsRecon[h] = False



            print(json.dumps(generateSubjectsRecon,indent=2))


            time.sleep(0.5)


        i['generateSubjectsRecon'] = generateSubjectsRecon
        json.dump(data,open('metadata_alan-lomax-in-michigan.json','w'),indent=2)
        

    else:

        todel = []
        new_generateSubjectsRecon = copy.deepcopy(i['generateSubjectsRecon']) 

        for h in i['generateSubjectsRecon']:

            if i['generateSubjectsRecon'][h] == False:



                r = do_search_naf(h)

                if r != False:
                    new_generateSubjectsRecon[h] = r
                    # print(i['generateSubjectsRecon'][h])

                else:


                    # new_term  = h.replace(' in music','')
                    # new_term  = h.replace(' in literature','')
                    new_term = h.split(' in ')[0].strip()

                    r = do_search(new_term)

                    if r != False:
                        print("!!!!")
                        print(h)
                        print(r)
                        todel.append(h)

                        new_generateSubjectsRecon[new_term] = r
                        del new_generateSubjectsRecon[h]

                    # else:



                time.sleep(0.5)

        # print(json.dumps(new_generateSubjectsRecon,indent=2))
        i['generateSubjectsRecon'] = new_generateSubjectsRecon

        # for d in todel:
        #     del i['generateSubjectsRecon'][d]

    # elif 'headings' in subjects:
    #     i['generateSubjects'] = subjects['headings']

    json.dump(data,open('metadata_alan-lomax-in-michigan.json','w'),indent=2)




        


