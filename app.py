from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv() # For using environment variables


OPENAI_API_KEY = os.environ["OPENAI_API_KEY"] # load openai's api key

client = OpenAI()

while True:
    question = input("User: ")
    if question != "bye":

        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            max_tokens=50, # Maximum num of takens get as response
            n=1, # No.of response
            temperature=0, # Randomness of the response
            messages=[
                {"role": "user", "content": question}
            ]
        )

        # print(response)

        for choice in response.choices:
            print(f"AI: {choice.message.content}")

    else:
        print("AI: Bye...")
        break


