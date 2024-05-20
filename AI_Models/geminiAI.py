import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))




# API key obtained from Google AI Studio
api_key = "AIzaSyCtdsOTBr6cr-NKiveIaT87LeJE4eglMpk"

genai.configure(api_key=api_key)


model = genai.GenerativeModel("gemini-1.5-flash-latest")

message = "poetry of Allama Iqbal"

response = model.generate_content(message)
print("response text===>", response.text)
