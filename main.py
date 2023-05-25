import openai
import json

from prompts import gen_prompt

key = open('./key.txt', 'r')

openai.api_key  = key.readline()

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.2,
    )
    return response.choices[0].message["content"]

def create_lp(text):
    lp = open('plan.txt', 'w')
    lp.write(text)
    lp = open('./plan.txt', 'r')
    lp.read()

def main():
    input_str = input('Enter your topics for the learning plan: ')
    print("*** GENERATING ***")
    prompt = gen_prompt(input_str)
    response = get_completion(prompt)
    create_lp(response)
    print("** DONE **")


main()