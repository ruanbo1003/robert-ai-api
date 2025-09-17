#
# # pip install https://github.com/KittenML/KittenTTS/releases/download/0.1/kittentts-0.1.0-py3-none-any.whl
#
# import os
# from kittentts import KittenTTS
# import soundfile as sf
#
# words = [
#     "dog",
#     "cat",
#     "fish",
#     "elephant",
#     "snake",
#     "lion",
#     "tiger",
#     "bear",
# ]
#
# # available_voices : [  'expr-voice-2-m', 'expr-voice-2-f', 'expr-voice-3-m', 'expr-voice-3-f',  'expr-voice-4-m', 'expr-voice-4-f', 'expr-voice-5-m', 'expr-voice-5-f' ]
# voices = [
#     'expr-voice-2-m',
#     'expr-voice-2-f',
#     'expr-voice-3-m',
#     'expr-voice-3-f',
#     'expr-voice-4-m',
#     'expr-voice-4-f',
#     'expr-voice-5-m',
#     'expr-voice-5-f'
# ]
#
# m = KittenTTS("KittenML/kitten-tts-nano-0.2")
#
# for word in words:
#     for voice in voices:
#         output_dir = f"output/{voice}"
#         os.makedirs(output_dir, exist_ok=True)
#
#         audio = m.generate(text=word, voice=voice )
#         sf.write(f'{output_dir }/{word}.wav', audio, 24000) # save each audio file

from kittentts import KittenTTS
m = KittenTTS("KittenML/kitten-tts-nano-0.2")

audio = m.generate("This high quality TTS model works without a GPU", voice='expr-voice-2-f' )

# available_voices : [  'expr-voice-2-m', 'expr-voice-2-f', 'expr-voice-3-m', 'expr-voice-3-f',  'expr-voice-4-m', 'expr-voice-4-f', 'expr-voice-5-m', 'expr-voice-5-f' ]

# Save the audio
import soundfile as sf
sf.write('output.wav', audio, 24000)