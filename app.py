import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv('KEY')


def BasicGeneration(userPrompt):
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=userPrompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,

    )
    return completion.choices[0].text.strip()

prompt = "please explain BFS " + "as if I'm in grade school. Provide examples when possible in javascript"
response = BasicGeneration(prompt)
print(response)
