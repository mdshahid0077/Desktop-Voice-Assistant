import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks."},
        {"role": "user", "content": "what is coding"}
    ]
)

print(completion.choices[0].message.content)
