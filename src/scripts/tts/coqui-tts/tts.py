from Cython.Compiler.Naming import import_star

# pip install TTS

import os
from TTS.api import TTS
device = 'cpu'
print(TTS().list_models())

words = [
    "dog",
    "cat",
    "fish",
    "elephant",
    "snake",
    "lion",
    "tiger",
    "bear",
]

models = [
    'tts_models/en/ljspeech/glow-tts',
    'tts_models/en/ljspeech/tacotron2-DDC',
    'tts_models/en/ljspeech/fast_pitch',
]

for model in models:
    output_dir = f"output/{model.split('/')[-1]}"
    os.makedirs(output_dir, exist_ok=True)

    for word in words:
        tts = TTS(model).to(device)
        tts.tts_to_file(text=word, file_path=f"{output_dir}/{word}.wav")
