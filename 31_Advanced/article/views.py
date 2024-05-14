from django.views.generic.list import ListView
from .models import Article

# Articles : Page HTML affichant sous forme de table HTML tous les champs (à
# l’exception de content) de tous les articles enregistrés dans la table Article.
# Le tableau doit disposer d’un header indiquant le titre de chaque colonne.


class ArticleView(ListView):
    model = Article
    paginate_by = 100
    template_name = "article/templates/article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PublicationsView(ListView):
    model = Article
    paginate_by = 100
    template_name = "article/templates/publications_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Article.objects.filter(author=self.request.user)
        return context
