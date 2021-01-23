from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from accounts_api.models import UserProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')
    name = forms.CharField(max_length=254, help_text='Requred. Enter a unique username')

    class Meta:
        model = UserProfile
        # fields = ('email', 'name', 'password1', 'password2',)
        fields = ('name', 'email', 'password1', 'password2',)



class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('email', 'name', )

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            account = UserProfile.objects.exclude(pk=self.instance.pk).get(email=email)
        except UserProfile.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

