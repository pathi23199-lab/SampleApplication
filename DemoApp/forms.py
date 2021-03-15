from django import forms

from DemoApp.models import User_Json
class User_JsonForm(forms.ModelForm):
    userId = forms.CharField(initial=" fgs", widget=forms.HiddenInput())
    ID = forms.CharField(initial=" fgs", widget=forms.HiddenInput())
    title = forms.CharField(initial=" fgs", widget=forms.HiddenInput())
    body = forms.CharField(initial = " fgs",widget=forms.HiddenInput())
    class Meta:
        model=User_Json
        fields = '__all__'
        # fields=('docfile','body')

