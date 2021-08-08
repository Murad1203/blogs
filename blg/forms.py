from django import forms
from .models import BlogApps

class BlogsForm(forms.ModelForm):
    class Meta:
        model = BlogApps
        fields = ['title', 'content','photo', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows':5}),
            'category': forms.Select(attrs={'class': 'form-control'}),

            'photo': forms.FileInput(attrs={'class': 'form-control'}),

        }
