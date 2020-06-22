from django import forms
from .models import Deal

class create(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ('title', 'image', 'address', 'more','price')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget = forms.widgets.FileInput()
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


