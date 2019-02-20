from django.contrib import admin

# Register your models here.

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"] #things to display
    list_display_links = ["updated"] # makes the link
    list_editable=["title"]
    list_filter=["title", "timestamp"]
    search_fields=["title"]

    class Meta:
        model = Post


admin.site.register(Post,PostModelAdmin) #built in admin function that registers post model in admin site