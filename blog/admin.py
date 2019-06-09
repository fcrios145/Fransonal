from django import forms
from django.contrib import admin

from blog.widgets import HtmlEditor
from blog.models import Post


class AppAdminForm(forms.ModelForm):
    model = Post

    class Meta:
        fields = ('title', 'description', 'short_summary', 'public',)
        widgets = {
            'description': HtmlEditor(attrs={'style': 'width: 30%; height: 800px !important;'}),
        }


class AppAdmin(admin.ModelAdmin):
    form = AppAdminForm


admin.site.register(Post, AppAdmin)
