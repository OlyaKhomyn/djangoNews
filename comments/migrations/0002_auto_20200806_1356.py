# Generated by Django 3.1 on 2020-08-06 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="comment", unique_together={("id", "post")},
        ),
    ]