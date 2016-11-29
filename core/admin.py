from django.contrib import admin

from core.models import Publishes


class PublishesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'user_name')


admin.site.register(Publishes, PublishesAdmin)
