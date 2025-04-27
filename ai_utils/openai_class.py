import time

from config import get_settings
from openai import OpenAI, RateLimitError

import os

# Set proxy
os.environ["HTTP_PROXY"] = "http://pr.sspx.ru:8888"
os.environ["HTTPS_PROXY"] = "http://pr.sspx.ru:8888"

client = OpenAI(api_key=get_settings().OPENAI_API_KEY)

for _ in range(3):  # Try up to 3 times
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What's the capital of France?"},
            ],
        )
        print(response.choices[0].message.content)
        break
    except RateLimitError:
        print("Rate limit hit. Waiting 10 seconds before retrying...")
        time.sleep(10)
