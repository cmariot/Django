from django.shortcuts import render
from django import forms
from datetime import datetime


def form(request):

    if request.method == "POST":
        form = forms.Form(request.POST)
        if form.is_valid():
            current_date = str(datetime.now()).replace("\n", " ") + " " + " "
            with open("ex02/file.txt", "a") as f:
                f.write(current_date + request.POST["text"] + "\n")
            return result(request)

    elif request.method == "GET":
        class MyForm(forms.Form):
            text = forms.CharField(label="Text", max_length=100)
        context = {"form": MyForm()}
        return render(request, "form.html", context)


def result(request):

    with open("ex02/file.txt", "r") as f:
        text = f.read().split("\n")
    context = {"result": text}
    return render(request, "result.html", context)
