from django import forms
from .models import person
class pf (forms.Form):
    f1=forms.CharField(label='to do name')
    f2=forms.CharField(label='to-do')
#npf=new person form
class npf (forms.ModelForm):
    class Meta:
        model=person
        fields=('first_name','last_name')
