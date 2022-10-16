from django import forms

class DecimalPointForm(forms.Form):
    dp = forms.IntegerField(label='Number of decimal points', max_value=100000)