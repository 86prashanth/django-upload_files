from django import forms
from .models import Upload_files

class Upload_form(forms.ModelForm):
    class Meta:
        model=Upload_files
        fields=['author','title','file','image']