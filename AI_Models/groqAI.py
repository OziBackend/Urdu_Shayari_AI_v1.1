# key=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

import os
os.environ["GROQ_API_KEY"] = "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"  # Replace with your actual key
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def generate_prompt():
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "I want to generate Allama Iqbal's poetry 'Shikwa' in Urdu text. each stanza on new line. There should be no english in between, and no urdu other than the poetry. The format should be in following format:['first stanza ',  'second stanza', 'third stanza', 'fourth stanza', 'fifth stanza',......]",
            }
        ],
        # model=" llama3-8b-8192",
        # model=" llama3-70b-8192",
        # model="mixtral-8x7b-32768",
        model="gemma-7b-it",
        # model="whisper-large-v3",
    )
    return chat_completion


def groqAI():
    chat_completion = generate_prompt()
    return(chat_completion.choices[0].message.content)