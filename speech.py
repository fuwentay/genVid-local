from gtts import gTTS
from mutagen.mp3 import MP3
import os

# Generates mp3 files for the sentence.
def text_to_speech(text):    
    myobj = gTTS(
        text=text, 
        lang='en', 
        slow=False
        )
    
    try:
        os.mkdir("/tmp/audio")
    except FileExistsError:
        print("Audio folder already exists.")

    myobj.save("/tmp/audio/" + text[:10] + ".mp3")

# text = 'If the sun were to start to disintegrate, the first thing we would see is a rapid decrease in the luminosity of the star, as its energy production would begin to diminish'
# text_to_speech(text)

def text_to_speech_overall(text):    
    myobj = gTTS(
        text=text, 
        lang='en', 
        slow=False
        )
    
    myobj.save("/tmp/" + text[:10] + ".mp3")

# Returns a list of all the mp3 durations
def get_all_mp3_duration(sentences_lst):
    # FIXME: can clean up code. a lot of duplicate components due to this order lst (for both speech and video stitching)
    order = []
    for sentence in sentences_lst:
        order.append(sentence[:10] + ".mp3")

    duration_list = []
    for file in order:
        path = "/tmp/audio/"
        audio = MP3(path + file)
        duration_list.append(audio.info.length)
    print(duration_list)
    return duration_list

def get_mp3_duration(file):
    audio = MP3(file)
    print(audio.info.length)
    return audio.info.length

# get_mp3_duration("audio\welcome.mp3")