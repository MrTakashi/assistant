from openai import OpenAI
from config import get_settings
settings = get_settings()

from openai import OpenAI

client = OpenAI(
    api_key=settings.PROXYAPI_KEY,
    base_url="https://api.proxyapi.ru/openai/v1",
)

chat_completion = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {
            "role": "system",
            "content": "Определи язык запроса и обязательно ответь на том же языке."
        },
        {
            "role": "user",
            # "content": "Tell me a joke"
            # "content": "Hazil ayting"
            "content": "Расскажи анекдот"
        },
    ]
)

print(chat_completion.choices[0].message.content)
