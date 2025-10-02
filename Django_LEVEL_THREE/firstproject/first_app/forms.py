from django import forms

class Formname(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Text = forms.CharField(widget=forms.Textarea)