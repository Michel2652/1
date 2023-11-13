from django import forms

class user_r_f(forms.Form):
    username=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField()
    first_name=forms.CharField(label='first name')
    last_name=forms.CharField(label='last name')


class user_l_f(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
