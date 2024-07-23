from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_tip, name="post_tip"),
    path("remove/<int:tip_id>/", views.remove_tip, name="remove_tip"),
    path("upvote/<int:tip_id>/", views.upvote_tip, name="upvote_tip"),
    path("downvote/<int:tip_id>/", views.downvote_tip, name="downvote_tip"),
]
