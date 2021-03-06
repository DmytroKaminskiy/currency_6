import uuid

from django import forms
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse


class UserSignUpForm(forms.ModelForm):

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'password1',
            'password2',
        )

    def clean(self):
        cleaned_data: dict = super().clean()
        if not self.errors:
            if cleaned_data['password1'] != cleaned_data['password2']:
                raise forms.ValidationError('Passwords should match!')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)  # User(...) but do not save to database
        # user.password = self.cleaned_data['password1']
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        # user.email = user.email.lower()
        user.username = str(uuid.uuid4())
        user.save()  # <- save user to database
        self._send_email()
        return user

    def _send_email(self):
        subject = 'Thanks for sign up'
        path = reverse('account:activate', args=(self.instance.username, ))
        body = f'''
        {settings.HTTP_SCHEMA}://{settings.DOMAIN}{path}
        '''
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [self.instance.email],
            fail_silently=False,
        )
