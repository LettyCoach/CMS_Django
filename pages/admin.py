# from translations.admin import TranslatableAdmin, TranslationInline
from django.contrib import admin
from .models import Page, Comment


class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('lang', "body", "created_at")


admin.site.register(Comment, CommentAdmin)
admin.site.register(Page, PageAdmin)
