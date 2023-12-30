import os
# from dotenv import load_dotenv
import openai
from prompt import SQLprompt
from openai import OpenAI


# load_dotenv()
client = OpenAI(
    # This is the default and can be omitted
    api_key="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",
)
# completion = openai.ChatCompletion()


start_chat_log = [
    {"role": "system", "content": SQLprompt },
]


def askgpt(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    chat_log = chat_log + [{'role': 'user', 'content': question}] 
    response = client.chat.completions.create( messages=chat_log , model='gpt-3.5-turbo',)
    answer = response.choices[0].message.content
    chat_log = chat_log + [{'role': 'assistant', 'content': answer}]
    return answer