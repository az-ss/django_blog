from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Publishes(models.Model):
    title = models.TextField(max_length=30)
    content = models.TextField()
    user_name = models.TextField(max_length=30)

    def __str__(self):
        return "Title: {0}\nContent: {1}\nPosted by: {2}".format(self.title, self.content, self.user_name)
