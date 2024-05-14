from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article

# Articles : Page HTML affichant sous forme de table HTML tous les champs (à
# l’exception de content) de tous les articles enregistrés dans la table Article.
# Le tableau doit disposer d’un header indiquant le titre de chaque colonne.


class ArticleList(ListView):
    model = Article
    template_name = "article/templates/article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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
