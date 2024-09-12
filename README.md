# lomax-michigan-whisper
lomax-michigan


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

