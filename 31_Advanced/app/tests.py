from django.test import TestCase, Client
from django.urls import reverse
from user.models import User
from article.models import Article, UserFavoriteArticle


class ViewAccessTests(TestCase):

    def setUp(self):
        # Configuration d'un client de test
        self.client = Client()

        # Création d'un utilisateur de test
        self.user = User.objects.create_user(
            username='testuser', password='abcde0123'
        )

        # Définir les URLs des vues à tester
        self.urls = {
            'favorites': reverse('favorites'),
            'publications': reverse('publications'),
            'publish': reverse('publish')
        }

    def test_views_redirect_if_not_logged_in(self):
        """
        Teste si les vues nécessitant une connexion redirigent l'utilisateur
        vers la page de connexion.
        """
        self.client.logout()
        for name, url in self.urls.items():
            response = self.client.get(url)
            redirect_url = reverse('login') + f'?next={url}'
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, redirect_url)
            self.assertRedirects(response, redirect_url)

    def test_views_accessible_if_logged_in(self):
        """
        Teste si les vues nécessitant une connexion sont accessibles une fois
        l'utilisateur connecté.
        """
        self.client.login(username='testuser', password='abcde0123')
        for name, url in self.urls.items():
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)


class UserCreationFormAccessTests(TestCase):

    def setUp(self):
        # Configuration d'un client de test
        self.client = Client()

        # Création d'un utilisateur de test
        self.user = User.objects.create_user(
            username='testuser', password='abcde0123'
        )

        # URL de la vue de création d'utilisateur
        self.urls = {
            'register': reverse('register'),
            'login': reverse('login')
        }

    def test_user_creation_form_not_accessible_to_logged_in_users(self):

        # Connecter l'utilisateur de test
        self.client.login(username='testuser', password='abcde0123')

        for name, url in self.urls.items():

            # Tenter d'accéder au formulaire de création d'un nouvel utilisateur
            response = self.client.get(url)

            # Vérifier que l'utilisateur est redirigé
            self.assertNotEqual(response.status_code, 200)
            self.assertEqual(response.status_code, 302)

            # Vérifier la redirection vers la page d'accueil
            self.assertEqual(response.url, '/')

    def test_user_creation_form_accessible_to_anonymous_users(self):

        self.client.logout()

        for name, url in self.urls.items():

            # Tenter d'accéder au formulaire de création d'un nouvel utilisateur
            response = self.client.get(url)

            # Vérifier que l'utilisateur peut accéder au formulaire
            self.assertEqual(response.status_code, 200)


class UserMultipleFavoriteArticle(TestCase):

    def setUp(self):
        # Configuration d'un client de test
        self.client = Client()

        # Création d'un utilisateur de test
        self.user = User.objects.create_user(
            username='testuser', password='abcde0123'
        )

    def test_add_favorite_article(self):
        """
        Teste l'ajout d'un article aux favoris de l'utilisateur de multiples
        fois.
        """

        self.client.login(username='testuser', password='abcde0123')

        # Créer un nouvel article
        new_article = Article.objects.create(
            title='New Article 2',
            synopsis="Synopsis",
            content='This is a new article.',
            author=self.user
        )

        # URL de la vue d'ajout d'un article aux favoris
        url = reverse('add_to_favorites', args=[new_article.id])

        # Ajouter l'article aux favoris
        self.client.post(url)

        # Vérifier que l'article a été ajouté aux favoris
        self.assertTrue(UserFavoriteArticle.objects.filter(
            user=self.user, article=new_article
        ).exists())

        nb = UserFavoriteArticle.objects.filter(
            user=self.user, article=new_article
        ).count()

        self.assertEqual(nb, 1)

        # Ajouter l'article aux favoris une deuxième fois
        self.client.post(url)
        self.client.post(url)
        self.client.post(url)
        self.client.post(url)
        self.client.post(url)

        # Vérifier que l'article n'a pas été ajouté aux favoris une deuxième fois
        nb = UserFavoriteArticle.objects.filter(
            user=self.user, article=new_article
        ).count()

        self.assertEqual(nb, 1)
