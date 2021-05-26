#from Django import forms
from django import forms
class Subscribe(forms.Form):
    Email = forms.EmailField()

    def __str__(self):
        return self.Email
    
class SignUp(forms.Form):
    first_name = forms.CharField(help_text='Write your First Name' )
    last_name = forms.CharField()
    email = forms.EmailField(help_text = 'write your email', )
    Address = forms.CharField(required = False, )
    Technology = forms.CharField(initial = 'Django', disabled = True, )
    age = forms.IntegerField()
    password = forms.CharField(widget = forms.PasswordInput)
    re_password = forms.CharField(help_text = 'renter your password', widget = forms.PasswordInput)