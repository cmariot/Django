from django.shortcuts import render
from django import forms
from datetime import datetime
from django.conf import settings


def form(request):
    if request.method == "POST":
        form = forms.Form(request.POST)
        if form.is_valid():
            current_date = str(datetime.now()).replace("\n", " ") + " " + " "
            log_file_path = settings.LOG_FILE_PATH
            with open(log_file_path, "a") as f:
                f.write(current_date + request.POST["text"] + "\n")
            return result(request)

    elif request.method == "GET":
        class MyForm(forms.Form):
            text = forms.CharField(label="Text", max_length=100)
        context = {"form": MyForm()}
        return render(request, "ex02/templates/form.html", context)


def result(request):
    log_file_path = settings.LOG_FILE_PATH
    with open(log_file_path, "r") as f:
        text = f.read().split("\n")
    context = {"result": text}
    return render(request, "ex02/templates/result.html", context)
