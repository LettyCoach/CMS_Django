from django.contrib import admin
from .models import New


class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(New, NewAdmin)
