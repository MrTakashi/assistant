from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from config import get_settings
from personal_assistant_chat.DATASETS import TOPICS

settings = get_settings()

from openai import OpenAI
client = OpenAI(
    api_key=settings.PROXYAPI_KEY,
    base_url="https://api.proxyapi.ru/openai/v1",
)


@csrf_exempt
def home(request):
    response_text = ""
    context = {
        'response': None,
        'topics': TOPICS,
    }
    if request.method == "POST":
        user_input = request.POST.get("user_input")


        chat_completion = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {
                    "role": "system",
                    "content": "Определи язык запроса и обязательно ответь на том же языке."
                },
                {
                    "role": "user",
                    # "content": "Расскажи анекдот"
                    "content": user_input
                },
            ]
        )

        context['response'] = chat_completion.choices[0].message.content
        # for _ in chat_completion.choices:
        #     print(_.message.content)


    return render(
        request,"personal_assistant_chat/ai.html", context)


@csrf_exempt
def chat_no_design(request):
    response_text = ""

    if request.method == "POST":
        user_input = request.POST.get("user_input")


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
                    # "content": "Расскажи анекдот"
                    "content": user_input
                },
            ]
        )

        response_text = chat_completion.choices[0].message.content
        # for _ in chat_completion.choices:
        #     print(_.message.content)


    return render(request, "personal_assistant_chat/chat_no_design.html", {"response": response_text})
