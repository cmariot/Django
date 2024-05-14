from django.http import HttpResponseRedirect


# Decorator to check if user is logged
def is_logged_in(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect("/login")

    return wrapper
