import os
import openai
import sys

openai.api_key = ""

if __name__ == "__main__":
    if len(sys.argv) > 1:
      text = sys.argv[1]

      response = openai.Completion.create(
        engine="davinci-instruct-beta-v3",
        prompt="Write blog based on topic\n\n {}".format(text),
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
      )
      response = response['choices'][0]['text']
      print(response)
