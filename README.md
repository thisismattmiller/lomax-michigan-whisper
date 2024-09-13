# lomax-michigan-whisper


Check out this blog post to learn more: https://thisismattmiller.com/post/lomax-whisper/



### Get Whisper.cpp ready

We're downloading most of the models here to try each.

```
git clone https://github.com/ggerganov/whisper.cpp.git
cd whisper.cpp
make
./models/download-ggml-model.sh base
./models/download-ggml-model.sh small
./models/download-ggml-model.sh medium
./models/download-ggml-model.sh large-v1
./models/download-ggml-model.sh large-v2
./models/download-ggml-model.sh large-v3

```

### Index of Scripts

Runs Whisper over the files
* [run_whisper.py](run_whisper.py)

Enrichment / QA
* [gpt_subjects.py](gpt_subjects.py)
* [gpt_translate.py](gpt_translate.py)
* [reconcile_subjects.py](reconcile_subjects.py)
* [review_subjects.py](review_subjects.py)
* [add_lang.py](add_lang.py)
* [clean_up_vtt.py](clean_up_vtt.py)
* [build_qa_json.py](build_qa_json.py)
* [build_qa_best_choice.py](build_qa_best_choice.py)


Metadata
* [metadata_alan-lomax-in-michigan.json](metadata_alan-lomax-in-michigan.json)

Downloads Data from loc.gov
* [download_media.py](download_media.py)
* [download_metadata.py](download_metadata.py)

