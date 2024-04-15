from django.http import HttpResponse, Http404
from django.template import loader


def index(request):
    """
    A view that renders the index page located at ex00/templates/index.html.

    """
    try:
        template = loader.get_template("index.html")
        context = {}
        return HttpResponse(template.render(context, request))
    except loader.TemplateDoesNotExist as template_name:
        raise Http404(f"Template {template_name} does not exist.")
