from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    content = models.TextField()
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=100, db_index=True)

