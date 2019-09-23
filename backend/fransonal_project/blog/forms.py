from django.forms import ModelForm, TextInput, Select, FileInput, SelectMultiple, HiddenInput, Textarea
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'raw_content', 'status', 'hero_image', 'tags', 'short_content']
        widgets = {
            'name': TextInput(attrs={'class': 'sidebar--control select-css'}),
            'status': Select(attrs={'class': 'sidebar--control select-css'}),
            'hero_image': FileInput(attrs={'class': 'sidebar--control select-css'}),
            'tags': SelectMultiple(attrs={'class': 'sidebar--control sidebar--control--multiselect select-css'}),
            'raw_content': HiddenInput(),
            'short_content': Textarea(attrs={'class': 'sidebar--control select-css'})
        }