import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_gpt_response(prompt):
  response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=150,
      n=1,
      stop=None,
      temperature=0.7,
  )
  return response.choices[0].text.strip()


def main():
  print("Text Generator")
  while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
      print("Bye!")
      break
    response = get_gpt_response(user_input)
    print(response)


if __name__ == "__main__":
  main()
