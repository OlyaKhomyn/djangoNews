from django.db import models
from posts.models import Post


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    class Meta:
        unique_together = ["id", "post"]
