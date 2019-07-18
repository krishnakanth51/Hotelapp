from django import forms

class registration(forms.Form):
    student_name=forms.CharField(max_length=52)
    branch=forms.CharField(max_length=52)
    username=forms.CharField(max_length=52)
    password=forms.CharField(max_length=22)



class login(forms.Form):
    username=forms.CharField(max_length=44)
    password=forms.CharField(max_length=77)


    