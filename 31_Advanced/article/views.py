from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article, UserFavoriteArticle
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django import forms


class ArticleList(ListView):

    model = Article
    template_name = "article/templates/article_list.html"


class UserArticles(LoginRequiredMixin, ListView):

    model = Article
    template_name = "article/templates/publications_list.html"

    login_url = "/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not self.request.user.is_authenticated:
            context["object_list"] = []
        else:
            context["object_list"] = Article.objects.filter(
                author=self.request.user
            )
        return context


class ArticleDetail(DetailView):

    model = Article
    template_name = "article/templates/article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_favorite"] = False
        if self.request.user.is_authenticated:
            context["is_favorite"] = UserFavoriteArticle.objects.filter(
                user=self.request.user, article=self.object
            ).exists()
        return context


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'synopsis', 'content']
        labels = {
            'title': _('Title'),
            'synopsis': _('Synopsis'),
            'content': _('Content'),
        }


class PublishArticle(LoginRequiredMixin, CreateView):

    model = Article
    form_class = ArticleForm
    template_name = "article/templates/publish_article.html"

    login_url = "/login/"

    extra_context = {
        "Title": _("Title"),
        "Synopsis": _("Synopsis"),
        "Content": _("Content"),
        "Publish": _("Publish"),
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        if not form.is_valid():
            return super().form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("publications")


class AddToFav(LoginRequiredMixin, CreateView):

    model = UserFavoriteArticle
    fields = []
    template_name = "article/templates/add_to_favorites.html"

    login_url = "/login/"

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            form.add_error(
                None,
                "You must be logged in to add articles to favorites."
            )
            return super().form_invalid(form)
        form.instance.user = self.request.user
        form.instance.article = Article.objects.get(pk=self.kwargs.get("pk"))
        if UserFavoriteArticle.objects.filter(
            user=form.instance.user, article=form.instance.article
        ).exists():
            return super().form_invalid(form)
        if not form.is_valid():
            return super().form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER", "/")


class RemoveFromFav(LoginRequiredMixin, DeleteView):

    model = UserFavoriteArticle

    login_url = "/login/"

    def get_object(self):
        article_id = self.kwargs.get("article_id")
        user_id = self.request.user.id
        return UserFavoriteArticle.objects.get(
            user_id=user_id, article_id=article_id
        )

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            form.add_error(
                None,
                "You must be logged in to remove articles from favorites."
            )
            return super().form_invalid(form)

        article_id = self.kwargs.get("article_id")
        user_id = self.request.user.id

        to_delete = UserFavoriteArticle.objects.filter(
            user_id=user_id, article_id=article_id
        )

        if not to_delete.exists():
            print("Article not in favorites")
            return super().form_invalid(form)

        if not form.is_valid():
            return super().form_invalid(form)

        # Set the UserFavoriteArticle to delete
        self.object = to_delete.first()

        return super().form_valid(form)

    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER", "/")


class UserFavoriteArticles(LoginRequiredMixin, ListView):

    model = UserFavoriteArticle
    template_name = "article/templates/favorites_list.html"

    login_url = "/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            context["object_list"] = []
        else:
            context["object_list"] = UserFavoriteArticle.objects.filter(
                user=self.request.user
            )
        return context
