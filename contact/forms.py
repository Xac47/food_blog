from django import forms

from contact.models import SubscribeEmail, GetInTouch


class SubscribeEmailForm(forms.ModelForm):
    class Meta:
        model = SubscribeEmail
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput({'class': 'email-input', 'placeholder': 'Your email'})
        }
        labels = {
            'email': ''
        }


class GetInTouchForm(forms.ModelForm):
    class Meta:
        model = GetInTouch
        fields = ('name', 'email', 'message')
        widgets = {
            'name': forms.TextInput({'placeholder': 'Name'}),
            'email': forms.EmailInput({'placeholder': 'Email'}),
            'message': forms.Textarea({'placeholder': 'Message'})
        }
        labels = {
            'name': '',
            'email': '',
            'message': '',
        }
