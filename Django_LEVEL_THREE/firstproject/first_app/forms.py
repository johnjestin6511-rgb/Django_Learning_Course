from django import forms
from django.core import validators



class Formname(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Verfiy_Email = forms.EmailField(label="Enter your email again:")
    Text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data["Email"]
        Vemail = all_clean_data["Verfiy_Email"]

        if email != Vemail:
            raise forms.ValidationError("Make sure Email Matchs!")
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data["botcatcher"]
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("I got you BOT!")
    #     return botcatcher