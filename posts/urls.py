from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views

urlpatterns = [
    path("posts/", views.PostsList.as_view()),
    path("posts/<int:pk>", views.PostDetail.as_view()),
    path("posts/upvote/<int:pk>/", views.Upvote.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
