from django.shortcuts import render
from user.views import get_user_data
from tips.forms.create_tips import CreateTipForm
from tips.views import _get_tips


def index(request):

    context = get_user_data(request)

    if request.user.is_authenticated:
        context["create_tip_form"] = CreateTipForm()
        context["tips_list"] = _get_tips(request.user)

    return render(request, "homepage/templates/index.html", context)
