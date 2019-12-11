from django import template
from gtts import gTTS
import os
import html2text
from urllib.request import urlopen


register = template.Library()

@register.simple_tag
def texttospeech(url):
     #if request.method == 'POST':
    f = urlopen(url)
    html = f.read()
    text = html2text.html2text(html)
    speech = gTTS(text= text, lang='en')
    speech.save("test.mp3")
    os.system("start test.mp3")
    #text = "tts activated"
    #return "test.mp3"
