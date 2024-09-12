
import json
data = json.load(open('qa_model.json','r'))



for k in data:

	d = data[k]
	use = 'ggml-medium'

	if d['lang'] == 'en':

		# does the medium have a high level of duplication
		dupe_diff = d['dupe_score']['ggml-medium'] - d['dupe_score']['ggml-large-v1']
		if dupe_diff > 5:
			use = 'ggml-large-v1'

			# but if the # of unique lines is more in the medium model go with that one instead
			if d['unique_count']['ggml-medium'] > d['unique_count']['ggml-large-v1']:
				use = 'ggml-medium'

	else:

		# if the v2 model has less duplication than the mendium then use it
		use = 'ggml-medium'
		if d['dupe_score']['ggml-medium'] >= 75:

			if d['unique_count']['ggml-large-v2'] > d['unique_count']['ggml-medium']:
				use = 'ggml-large-v2'


		



	# print(k,use)

	data[k]['use_model'] = use

json.dump(data,open('qa_model.json','w'),indent=2)