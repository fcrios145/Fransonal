from django.contrib import admin

# Register your models here.

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'description')


admin.site.register(Post, PostAdmin)
