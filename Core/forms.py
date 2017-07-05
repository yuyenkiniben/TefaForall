from django.contrib.auth.models import User
from Core.models import UserProfile
from django import forms


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # this is to make the inputted password be in ****

    class Meta:   # this is to define ur class that was created above
        model = User  # since we want to use the Users table in the database we link our form to it
        fields = ['username', 'password', 'email', 'last_name', 'first_name']  # we need only these from the user


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # this is to make the inputted password be in ****

    class Meta:   # this is to define ur class that was created above
        model = User  # since we want to use the Users table in the database we link our form to it
        fields = ['username', 'password']  # we need only these from the user


# this form will be filled by the user after creating his account (i.e. his profile pic etc)
class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # this is to make the inputted password be in ****

    class Meta:  # this is to define ur class that was created above
        model = UserProfile  # since we want to use the Users table in the database we link our form to it
        fields = ['gender', 'dateofbirth', 'levelofeducation', 'nationality', 'contact']


class PictureForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()


class ForgotpasswordForm(forms.Form):
    """Image upload form."""
    email = forms.EmailField()


class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    content = forms.Textarea()


class CreatePasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # this is to make the inputted password be in ****

    class Meta:
        model = User
        fields = [
             "password"
        ]


class DonateForm(forms.Form):
    amount = forms.IntegerField()
    email = forms.CharField()
    comment = forms.Textarea()
    phonenumber = forms.IntegerField()

