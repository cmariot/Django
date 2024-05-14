from django.shortcuts import render
from .forms import MessageForm
from django.http import HttpResponse
from openai import OpenAI


def index(request):

    context = {
        "form": MessageForm()
    }
    return render(request, "chat/templates/index.html", context)


def send(request):

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()

            form_content = form.cleaned_data["content"]

            # Point to the local server
            # client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

            # history = [
            #     {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
            #     {"role": "user", "content": f"{form_content}"},
            # ]

            # while True:
            #     completion = client.chat.completions.create(
            #         model="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
            #         messages=history,
            #         temperature=0.7,
            #         stream=True,
            #     )

            #     new_message = {"role": "assistant", "content": ""}

            #     for chunk in completion:
            #         if chunk.choices[0].delta.content:
            #             print(chunk.choices[0].delta.content, end="", flush=True)
            #             new_message["content"] += chunk.choices[0].delta.content

            #     history.append(new_message)

            # return HttpResponse("Success!")

            client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

            completion = client.chat.completions.create(
                model="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
                messages=[
                    {"role": "system", "content": "Always answer in rhymes."},
                    {"role": "user", "content": "Introduce yourself."}
                ],
                temperature=0.7,
            )

            print(completion.choices[0].message)

            return HttpResponse(completion.choices[0].message.content)

        return HttpResponse("Invalid form")