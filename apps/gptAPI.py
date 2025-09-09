from openai import OpenAI

key_api = "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"
client = OpenAI(
    api_key=key_api
    )

def gpt_reponse(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# ['choices'][0]['message']['content']
