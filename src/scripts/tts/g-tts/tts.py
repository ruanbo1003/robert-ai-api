
# pip install gTTS

from gtts import gTTS

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
two_words = [
    "two dogs",
    "two cats",
    "three fish",
    "two elephants",
    "two snakes",
]
# for word in words:
#     tts = gTTS(word, slow=True)
#     tts.save(f'output/{word}.mp3')

for two_word in two_words:
    tts = gTTS(two_word, slow=True)
    tts.save(f'output/two_words/{two_word.replace(" " , "_")}.mp3')
