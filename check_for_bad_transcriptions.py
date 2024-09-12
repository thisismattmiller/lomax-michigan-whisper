import webvtt
import glob
import shutil



for file in glob.glob('/Volumes/NextGlum/lc-lomax/converted/*.vtt'):

    total = 0
    bracket = 0
    for caption in webvtt.read(file):

        total+=1
        if caption.text.strip()[0] == '[':
            bracket+=1


    if bracket / total >= 0.9:

        file = file.split('/')[-1]

        print(file)
        filename = file.replace('.vtt','')
        shutil.move(f"/Volumes/NextGlum/lc-lomax/converted/{filename}", f"/Volumes/NextGlum/lc-lomax/converted_second_pass/{filename}")
        shutil.move(f"/Volumes/NextGlum/lc-lomax/converted/{file}", f"/Volumes/NextGlum/lc-lomax/converted_second_pass/{file}")


        # print(caption.start)
        # print(caption.end)
        # print(caption.text)