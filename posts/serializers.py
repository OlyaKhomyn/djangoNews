from rest_framework import serializers
from posts.models import Post
from comments.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "link",
            "created",
            "upvotes",
            "author_name",
            "comments",
        )

    def create(self, validated_data):
        title = validated_data.get("title")
        link = validated_data.get("link")
        author_name = validated_data.get("author_name")
        return Post.objects.create(title=title, link=link, author_name=author_name)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.link = validated_data.get("link", instance.link)
        instance.author_name = validated_data.get("author_name", instance.author_name)
        instance.save()
        return instance
