from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Records

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}))
    firstname = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First name'}))
    lastname = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last name'}))
     
    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname','email','password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].lable = ''
        self.fields['username'].help_text = '<span>Required 150 character</span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].lable = ''
        self.fields['password1'].help_text = '<span>you need put it with your password!@#$%^&*()?/<></span>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].lable = ''
        self.fields['password2'].help_text = '<span>you need put it with your password!@#$%^&*()?/<></span>'

#Create add records form
class AddRecordForm(forms.ModelForm):
    firstname = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Firstname', 'class':'form-control'}), label="")
    lastname = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Lastname', 'class':'form-control'}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Email', 'class':'form-control'}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Phone', 'class':'form-control'}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Address', 'class':'form-control'}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'City', 'class':'form-control'}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'State', 'class':'form-control'}), label="")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Zipcode', 'class':'form-control'}), label="")

    class Meta:
        model = Records
        exclude = ('user',)