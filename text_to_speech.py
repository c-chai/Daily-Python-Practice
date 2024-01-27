# Create a program which turns text to speech from a webstie URL 
# It will be read directly and speech file will not be saved 

import io
import nltk
from newspaper import Article
from gtts import gTTS
import pygame
import time

def text_to_speech(url):
    # Download and parse the article
    article = Article(url)
    article.download()
    article.parse()
    nltk.download('punkt', quiet=True)
    article.nlp()

    # Convert article text to speech
    language = 'en'
    my_obj = gTTS(text=article.text, lang=language, slow=False)

    # Use an in-memory bytes buffer instead of a physical file 
    mp3_fp = io.BytesIO()
    my_obj.write_to_fp(mp3_fp)
    mp3_fp.seek(0)  # Go to the beginning of the in-memory file

    # Initialize pygame and play the speech
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_fp)
    pygame.mixer.music.play()

    # Wait for the user to stop the playback
    print("Press 'Enter' to stop the playback.")
    input()  # Wait for user to press Enter

    # Stop the playback
    pygame.mixer.music.stop()

if __name__ == '__main__':
    text_to_speech(
        url='https://www.yahoo.com/lifestyle/is-it-safe-to-stand-in-front-of-a-microwave-while-its-on-heres-what-experts-say-200027745.html'
    )
