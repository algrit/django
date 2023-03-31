from django import forms
from .models import Feedback

# class FeedbackForm(forms.Form):
#     name = forms.CharField(label='Name', min_length=2, max_length=15, error_messages={
#         "max_length": "Слишком много символов, должно быть %(limit_value)d, сейчас символов %(show_value)d.",
#         "min_length": "Слишком мало символов, должно быть %(limit_value)d, сейчас символов  %(show_value)d.",
#         "required": "Обязательно к заполнению"})
#
#     surname = forms.CharField()
#     feedback = forms.CharField(widget=forms.Textarea(attrs={"cols": "20", "rows": "2"}))
#     rating = forms.IntegerField(label='Rating', min_value=1, max_value=5, error_messages={
#         'min_value': 'low',
#         'max_value': 'much',
#         'required': 'input damn rating'
#     })


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        labels = {'name': 'Name',
                  'surname': 'Surname'}
        error_messages = {'name':{
        "max_length": "Слишком много символов, должно быть %(limit_value)d, сейчас символов %(show_value)d.",
        "min_length": "ТЫ ЧЕ ЧЕПУШИЛО",
        "required": "Обязательно к заполнению"}}