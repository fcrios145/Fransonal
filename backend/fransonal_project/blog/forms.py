from django.forms import ModelForm, TextInput, Select, FileInput, SelectMultiple
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'raw_content', 'status', 'hero_image', 'tags']
        widgets = {
            'name': TextInput(attrs={'class': 'sidebar--control select-css'}),
            'status': Select(attrs={'class': 'sidebar--control select-css'}),
            'hero_image': FileInput(attrs={'class': 'sidebar--control select-css'}),
            'tags': SelectMultiple(attrs={'class': 'sidebar--control sidebar--control--multiselect select-css'}),
        }