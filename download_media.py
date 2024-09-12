import requests
import json
import os.path


def download_file(id):
	if os.path.isfile(f"/Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan/{id}.mp3") == True:
		return False
	# NOTE the stream=True parameter below
	with requests.get(f"https://tile.loc.gov/storage-services/media/afc/lomax/{id}.mp3", stream=True) as r:
		r.raise_for_status()
		with open(f"/Volumes/NextGlum/lc-lomax/alan-lomax-in-michigan/{id}.mp3", 'wb') as f:
			for chunk in r.iter_content(chunk_size=8192): 
				# If you have chunk encoded response uncomment if
				# and set chunk_size parameter to None.
				#if chunk: 
				f.write(chunk)
	return True






data = json.load(open('metadata_alan-lomax-in-michigan.json'))

for f in data:
	print(f['aka'][0].split('/')[-2])
	download_file(f['aka'][0].split('/')[-2])