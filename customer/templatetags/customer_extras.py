from django import template
from gtts import gTTS
import os


register = template.Library()

@register.simple_tag
def texttospeech(text):
     #if request.method == 'POST':
        speech = gTTS(text= text, lang='en')
        speech.save("test.mp3")
        os.system("start test.mp3")
        #text = "tts activated"
        #return "test.mp3"
