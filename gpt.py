import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
api_key = os.getenv("OPENAI_API_KEY")

# Specify the input filename
input_filename = "input/input1.txt"

# Read the content of the file
with open(input_filename, 'r') as file:
    input_text = file.read()


completion = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {"role": "system", "content": "You are a language assistant, given the plain text, give the grammar support for language learner."},
    {"role": "user", "content": input_text + "\n pick top 10 complicated sentences, and give grammar analysis for language learner, for each sentence,including vocab learning, sentence structure, main clause and main clause and other clauses, phrases（i.e. can't stop doing sth）, etc."}
  ]
)

output_text = completion.choices[0].message.content
# print(output_text)
# Specify the filename
filename = "output/output1.txt"

# Open the file in write mode and write the content
with open(filename, 'w') as file:
    file.write(output_text)

print(f"Output saved to {filename}")