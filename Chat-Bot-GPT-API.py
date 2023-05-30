import openai
import os

openai.api_key = "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"
os.environ['OPENAI_API_KEY'] = "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"

completion = openai.Completion()

chat_log = ''
question = 'Hi, How are you?'
while True:
    try:
        question = input("Human: ")
        prompt = f'{chat_log}Human:{question}\nAI:'

        response = completion.create(
            prompt = prompt, engine = "davinci", stop = ["\nHuman"], temperature = 0.9,
            top_p = 1, best_of = 1,
            max_tokens = 150)
        answer  = response.choices[0].text.strip()
        print("AI: \n"+ answer)
    except KeyboardInterrupt:
        break

