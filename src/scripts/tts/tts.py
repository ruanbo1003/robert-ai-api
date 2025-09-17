
# cmd: kokoro-tts input.txt dog.mp3 --lang en-us --voice af_kore --format mp3

# 对比下来，heart 效果会更好一些

from kokoro import KPipeline
import soundfile as sf


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
voices = [
    "af_alloy",
    "af_aoede",
    "af_bella",
    "af_heart",
    "af_jessica",
    "af_kore",
    "af_nicole",
    "af_nova",
    "af_river",
    "af_sarah",
    "af_sky"
]

# 🇺🇸 'a' => American English, 🇬🇧 'b' => British English
# 🇪🇸 'e' => Spanish es
# 🇫🇷 'f' => French fr-fr
# 🇮🇳 'h' => Hindi hi
# 🇮🇹 'i' => Italian it
# 🇯🇵 'j' => Japanese: pip install misaki[ja]
# 🇧🇷 'p' => Brazilian Portuguese pt-br
# 🇨🇳 'z' => Mandarin Chinese: pip install misaki[zh]
pipeline = KPipeline(lang_code='a') # <= make sure lang_code matches voice, reference above.

import os
print(os.getcwd())

for voice in voices:
    output_dir = f"output/{voice}"
    os.makedirs(output_dir, exist_ok=True)

    text = ",".join(words)
    generator = pipeline(
        words, voice=voice,
        speed=1, split_pattern=r','
    )
    for i, (gs, ps, audio) in enumerate(generator):
        print(i)  # i => index
        print(gs) # gs => graphemes/text
        print(ps) # ps => phonemes
        sf.write(f'output/{voice}/{gs}.wav', audio, 24000) # save each audio file
