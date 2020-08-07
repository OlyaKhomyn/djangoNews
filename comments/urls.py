from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from comments import views


urlpatterns = [
    path("comments/", views.CommentsList.as_view()),
    path("comments/<int:pk>", views.CommentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
