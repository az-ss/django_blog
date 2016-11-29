from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    title = models.TextField(max_length=50)
    content = models.TextField()
    user_name = models.TextField(max_length=30)
