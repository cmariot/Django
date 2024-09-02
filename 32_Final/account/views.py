from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, View
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm
from chat.models import ChatRoom


class AccountView(FormView, ListView):

    form_class = LoginForm
    template_name = 'account.html'
    success_url = reverse_lazy('account')

    model = ChatRoom
    context_object_name = 'chatrooms'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return JsonResponse(
            {
                'success': True,
                'errors': {},
                'username': self.request.user.username
            }
        )

    def form_invalid(self, form):
        return JsonResponse(
            {
                'success': False,
                'errors': form.errors
            }
        )


class LogoutView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        logout(request)
        return JsonResponse({'success': True})


class RegisterView(CreateView):

    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('account')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
