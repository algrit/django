from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        # exclude = ['something']
        labels = {'name': 'MyNameField'}
        error_messages = {
            'name': {
            'max_length': 'Too long Username, choose shorter'
            }
        }
