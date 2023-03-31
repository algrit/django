from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Name', min_length=2, max_length=20)
    rating = forms.IntegerField(label='Rating', min_value=1, max_value=10)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))
