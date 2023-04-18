import openai
import os
from dotenv import load_dotenv
# from pathlib import Path


load_dotenv()


openai.api_key = os.getenv('KEY')

# print("api key " + openai.api_key)
def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role" : "user", "content" : userPrompt}
        ]
    )
    return completion.choices[0].message.content

prompt = "what is a comet?"
response = BasicGeneration(prompt)
print(response)