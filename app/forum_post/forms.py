from django import forms
from .models import ForumPost


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'author', 'body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        # Auther is not required because it is automatically filled in by the view
        self.fields['body'].widget.attrs.update({'class': 'form-control'})
