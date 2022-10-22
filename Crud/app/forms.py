from django import forms
from django import forms
from .models import StuReg


class StuForm(forms.ModelForm):
    class Meta:
        model=StuReg
        fields = ['name','email','password']
        help_text={'name':'Enter Yout Name'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }