from django import forms
from .models import signup,Rent


class signupform(forms.ModelForm):
    class Meta:
        model = signup
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }


class loginform(forms.ModelForm):
    class Meta:
        model = signup
        fields = ('username','password')
        widgets = {
            'password': forms.PasswordInput(),
        }

class checkinform(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ('checkin','checkout')
     