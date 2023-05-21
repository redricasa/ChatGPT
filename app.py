
import os
from dotenv import load_dotenv
import openai
# from pathlib import Path


load_dotenv()


openai.api_key = os.getenv('KEY')

# print("api key " + openai.api_key)
def BasicGeneration(userPrompt):
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=userPrompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        log_level="info",
        # model = "gpt-3.5-turbo",
        # messages = [
        #     {"role" : "user", "content" : userPrompt}
        # ]
    )
    return completion.choices[0].text.strip()

prompt = "what is a comet"
response = BasicGeneration(prompt)
print(response)

# response = openai.Completion.create(
#     model="text-davinci-003", 
#     prompt="Say this is a test", 
#     temperature=0.6, 
#     max_tokens=150
#     )

# print(response.choices[0].text)