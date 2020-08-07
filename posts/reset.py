from posts.models import Post
from django.db import IntegrityError
from posts.error_logger import LOGGER


def reset_votes():
    posts = Post.objects.all()
    for post in posts:
        post.reset_votes()
        save_into_database(post)


def save_into_database(obj):
    try:
        obj.save()
    except IntegrityError as e:
        LOGGER.error(e)
