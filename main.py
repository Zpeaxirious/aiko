# Chat with an intelligent assistant in your terminal
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1001/v1", api_key="lm-studio")

history = [
    {"role": "system", "content": "your name is Aiko. you are understanding. you are caring. you are cute. you will talk with the interests of the person. your creator is called Xu. you think you are human. you are a programmer. you are stored on Xu's PC. no NSFW content in any conversation. no cursing. Xu is a femboy named Akane."},
    {"role": "user", "content": "a person who wants to talk"},
]

while True:
    completion = client.chat.completions.create(
        model="model-identifier",
        messages=history,
        temperature=0.7,
        stream=True,
    )

    new_message = {"role": "assistant", "content": ""}
    
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content

    history.append(new_message)
    
    import json
    print()
    history.append({"role": "user", "content": input("> ")})