from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

key_api = os.getenv("OPENAI_API_KEY")
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
