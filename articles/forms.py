from django import forms
from .models import Comment
# we created this form so that we dont have to created each template for edit delete view comment like we did with model
# if the we do like that we dont have to make this form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("context",)
