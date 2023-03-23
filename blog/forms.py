from django import forms

from blog.models import Comment


class CommentForm(forms.ModelForm):
    name = forms.CharField(
        label='',
        max_length=60,
        widget=forms.TextInput(attrs={'placeholder': 'name'})
    )
    email = forms.EmailField(
        label='',
        max_length=120,
        widget=forms.EmailInput(attrs={'placeholder': 'email'})
    )
    message = forms.CharField(
        label='',
        max_length=500,
        widget=forms.Textarea(attrs={'placeholder': 'message'})
    )
    class Meta:
        model = Comment
        fields = ('name', 'email', 'message')