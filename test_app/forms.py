from django import forms

class AdditionForm(forms.Form):
    a = forms.IntegerField(label="First number")
    b = forms.IntegerField(label="Second number")