from django.contrib import admin

from posts.models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "slug", "created_at")
    fields = ("author", "title", "slug", "text", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "slug", "text")
    raw_id_fields = ("author",)

#
# @admin.register(Tag)
# class PostAdmin(admin.ModelAdmin):
#     search_fields = ("title",)
