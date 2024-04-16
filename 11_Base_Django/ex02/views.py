from django.shortcuts import render
from datetime import datetime
from django.conf import settings
from .forms import MyForm
import os


def create_log_file(log_file_path):
    """
    Create the log file
    The log file path is defined in the settings
    """
    with open(log_file_path, "w") as f:
        f.write("")


def write_log(text):
    """
    Write a log in the log file
    The log file path is defined in the settings
    The date and time are added to the log before the text
    """
    with open(settings.LOG_FILE_PATH, "a") as f:
        f.write(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} - {text}\n")


def read_log(log_file_path):
    """
    Read the log file and return the content as a list of lines
    """
    if not os.path.exists(log_file_path):
        create_log_file(log_file_path)
    with open(log_file_path, "r") as f:
        file_content = f.read().split("\n")
    if file_content[-1] == "":
        file_content.pop()
    return file_content


def form(request):
    log_file_path = settings.LOG_FILE_PATH
    if request.method == "GET":
        form = MyForm()
    elif request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            write_log(form.cleaned_data["text"])
            form = MyForm()
    file_content = read_log(log_file_path)
    context = {
        "form": form,
        "historic": file_content,
    }
    return render(request, "ex02/templates/form.html", context)
