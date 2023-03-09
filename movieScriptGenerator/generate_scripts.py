import openai
import os
from time import sleep
import re

openai.api_key = os.getenv("OPENAI_KEY")

engine = "text-davinci-002"


def generate_scripts(
    prompt,
    max_tokens=250,
    temperature=1.1,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["absb"],
):
    max_rety = 5
    retry = 0
    while True:
        try:
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
                stop=stop,
            )
            text = response["choices"][0]["text"].strip()
            text = re.sub(r"\s+", " ", text)
            return text
        except Exception as oops:
            if retry < max_rety:
                retry += 1
                sleep(1)
            else:
                return print("Error Commnuicating with OpenAi: ", oops)


if __name__ == "__main__":
    for filename in os.listdir("premises"):
        with open("premises/%s" % filename, "r", encoding="utf-8") as f:
            premise = f.read()
        with open("prompt_script.txt", "r", encoding="utf-8") as f:
            prompt = f.read().replace("<<premise>>", premise)

        script = generate_scripts(prompt)
        print(script, "\n\n\n")
        new_filename = filename.replace("premise", "script")
        with open("scripts/%s" % new_filename, "w", encoding="utf-8") as f:
            f.write(script)
