from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].help_text = '<small>Required. 150 characters or fewer. Letters, digits and @.+-_ only.</small>'
        self.fields['username'].label = ''
        
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['email'].help_text = '<small>Required. Please provide any valid email address that you can access.</small>'
        self.fields['email'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].help_text = '<span class="form-text"><small><ul><li>Your password can’t be too similar to your username.</li><li>Your password can’t be a commonly used password.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be entirely numeric.</li></ul></small></span>'
        self.fields['password1'].label = ''
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].help_text = '<small>Enter the same password for verification.</small>'
        self.fields['password2'].label = ''

class ChangePassword(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].widget.attrs['placeholder'] = 'Current Password'
        self.fields['old_password'].help_text = ''
        self.fields['old_password'].label = ''
        
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password1'].help_text = '<span class="form-text"><small><ul><li>Your password can’t be too similar to your username.</li><li>Your password can’t be a commonly used password.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be entirely numeric.</li></ul></small></span>'
        self.fields['new_password1'].label = ''

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm New Password'
        self.fields['new_password2'].help_text = '<small>Enter the same password for verification.</small>'
        self.fields['new_password2'].label = ''

class ResetPassword(PasswordResetForm):
    class Meta:
        model = User
        fields = ('username', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].help_text = ''
        self.fields['username'].label = ''
        
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password1'].help_text = '<span class="form-text"><small><ul><li>Your password can’t be too similar to your username.</li><li>Your password can’t be a commonly used password.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be entirely numeric.</li></ul></small></span>'
        self.fields['new_password1'].label = ''

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm New Password'
        self.fields['new_password2'].help_text = '<small>Enter the same password for verification.</small>'
        self.fields['new_password2'].label = ''
