from django.contrib import admin

# Register your models here.

from .models import News, Menu


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "context", "get_image")
    list_filter = ["publish_date"]
    readonly_fields = ["get_image"]
    # search_fields = ["title", "context"]


admin.site.register(News, NewsAdmin)
admin.site.register(Menu)
