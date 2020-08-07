from django.db import models


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    link = models.URLField(max_length=250)
    created = models.DateField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=50)

    def upvote(self):
        self.upvotes += 1

    def reset_votes(self):
        self.upvotes = 0
