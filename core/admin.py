from django.contrib import admin

from core.models import Publishes
from core.models import UserProfile


class PublishesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'user_name')

admin.site.register(Publishes, PublishesAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'website')

admin.site.register(UserProfile, UserProfileAdmin)
