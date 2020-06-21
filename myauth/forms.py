from django import forms
from .models import User

class regForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('login', 'email', 'password')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.widgets.PasswordInput()
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class logForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('login', 'password')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.widgets.PasswordInput()
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

