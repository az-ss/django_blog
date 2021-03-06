from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Publishes(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user_name = models.CharField(max_length=30)

    def __str__(self):
        return "Title: {0}\nContent: {1}\nPosted by: {2}".format(self.title, self.content, self.user_name)


@python_2_unicode_compatible
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='static/profile_img', blank=True)

    def __str__(self):
        return self.user.username
