import pathlib
import textwrap
from googletrans import Translator

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def translate_text(text, dest_language='en'):
    translator = Translator()
    translated = translator.translate(text, dest=dest_language)
    return translated.text

#API key obtained from Google AI Studio
api_key = 'AIzaSyCtdsOTBr6cr-NKiveIaT87LeJE4eglMpk'

genai.configure(api_key=api_key)



model = genai.GenerativeModel('gemini-1.0-pro')

message="علامہ اقبال کی 'شکوہ' شاعری صرف پہلا بند"
translated_text = translate_text(message)
print('prompt===>',translated_text)

response = model.generate_content(translated_text)
print('response text===>',response.text)

response_text_urdu = translate_text(response.text, dest_language='ur')
print('urdu response===> \u202B',response_text_urdu)