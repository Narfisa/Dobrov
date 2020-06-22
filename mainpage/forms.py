from django import forms
from .models import Deal

class create(forms.ModelForm):
    class Meta:
        model = Deal
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget = forms.widgets.FileInput()
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


