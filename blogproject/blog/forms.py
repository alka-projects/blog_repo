from django import forms
from blog.models import Comment

class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.CharField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')
