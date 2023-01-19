# Django imports
from django import forms
from django.forms import TextInput, Select, FileInput


# Third part app imports
from ckeditor.widgets import CKEditorWidget


# Blog app imports
from blog.models.article_models import Article
from blog.models.category_models import Category


class ArticleCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(approved=True),
                                      empty_label="Select Category",
                                      widget=forms.Select(attrs={
                                          "class": "form-control selectpicker",
                                          "type": "text",
                                          "name": "article-category",
                                          "id": "articleCategory",
                                          "data-live-search": "true"
                                      }))

    class Meta:

        # Article status constants
        DRAFTED = "DRAFTED"
        PUBLISHED = "PUBLISHED"

        # CHOICE

        STATUS_CHOICES = (
            (DRAFTED, 'Draft'),
            (PUBLISHED, 'Publish'),
        )

        model = Article
        fields = ["title", "category", "image",
                  "image_credit", "body", "tags", "status"]

        widgets = {
            'title': TextInput(attrs={
                'name': 'article-title',
                'class': "form-control",
                'placeholder': "Enter Article Title",
                'id': "articleTitle"
            }),
            'image': FileInput(attrs={
                "class": "form-control clearablefileinput",
                "type": "file",
                "id": "articleImage",
                "name": "article-image"
            }),
        }
