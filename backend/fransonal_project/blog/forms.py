from django.forms import ModelForm, TextInput, Select, FileInput, SelectMultiple, HiddenInput, Textarea
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'raw_content', 'status', 'hero_image', 'tags', 'short_content']
        widgets = {
            'name': TextInput(attrs={'class': 'writter-sidebar__form__control writter-sidebar__form__control-black'}),
            'status': Select(attrs={'class': 'writter-sidebar__form__control writter-sidebar__form__control-black'}),
            'hero_image': FileInput(attrs={'class': 'writter-sidebar__form__control writter-sidebar__form__control-black'}),
            'tags': SelectMultiple(attrs={'class': 'writter-sidebar__form__control sidebasr--control--multiselect writter-sidebar__form__control-black'}),
            'short_content': Textarea(attrs={'class': 'writter-sidebar__form__control writter-sidebar__form__control-black'}),
            'raw_content': HiddenInput()
        }
        error_messages = {
            'raw_content': {
                'required': ("Favor de escribir algo en el editor :C"),
            },
        }