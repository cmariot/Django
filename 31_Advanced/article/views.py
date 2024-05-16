from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article, UserFavoriteArticle
from django.views.generic.edit import CreateView
from django.urls import reverse


class ArticleList(ListView):

    model = Article
    template_name = "article/templates/article_list.html"


class UserArticles(ListView):

    model = Article
    template_name = "article/templates/publications_list.html"

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
        return context


class PublishArticle(CreateView):

    model = Article
    fields = ["title", "synopsis", "content"]
    template_name = "article/templates/publish_article.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("publications")


class AddToFav(CreateView):

    model = UserFavoriteArticle
    fields = []
    template_name = "article/templates/add_to_favorites.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.article = Article.objects.get(pk=self.kwargs.get("pk"))
        if UserFavoriteArticle.objects.filter(
            user=form.instance.user, article=form.instance.article
        ).exists():
            print("Article already in favorites")
            return super().form_invalid(form)
        if not form.is_valid():
            return super().form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER", "/")


class UserFavoriteArticles(ListView):

    model = UserFavoriteArticle
    template_name = "article/templates/favorites_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            context["object_list"] = []
        else:
            context["object_list"] = UserFavoriteArticle.objects.filter(
                user=self.request.user
            )
        return context
