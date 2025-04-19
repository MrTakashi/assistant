import openai
import os
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render

openai.api_key = os.getenv("OPENAI_API_KEY")

# Create your views here.
@csrf_exempt
def chat_view(request):
    response_text = ""
    if request.method == "POST":
        user_message = request.POST.get("message")

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты вежливый и полезный ИИ-консьерж. Помогай людям выполнять простые задачи."},
                {"role": "user", "content": user_message},
            ]
        )
        response_text = completion.choices[0].message.content

    return render(request, "chat.html", {"response": response_text})
