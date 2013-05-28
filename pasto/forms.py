"""Forms for pasto"""

from django import forms

from .models import Code
from .highlight import LEXERS, DEFAULT_LEXER

class CodeForm(forms.ModelForm):

    def save(self, parent=None, *args, **kwargs):
        if parent:
            self.instance.parent = parent
        return super(CodeForm, self).save(*args, **kwargs)
    
    class Meta:
        model = Code
        fields = (
            'title',    
            'code',
            'lexer',
        )
