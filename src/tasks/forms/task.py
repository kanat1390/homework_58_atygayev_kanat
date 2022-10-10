from distutils.command.clean import clean
from wsgiref.validate import validator
from django import forms
from tasks.models import Task
from tasks.services import get_type_query_set
from django.utils.translation import gettext_lazy as _
from django.core.validators import BaseValidator
from ckeditor.widgets import CKEditorWidget

class TextFieldMinLengthValidator(BaseValidator):

    def __init__(self, limit_value, message=None):
        super().__init__(limit_value, message)
    
    def compare(self, a, b):
        return a <= b 
    
    def clean(self, x):
        return len(x)

class TextFieldMaxLengthValidator(BaseValidator):

    def __init__(self, limit_value, message=None):
        super().__init__(limit_value, message)
    
    def compare(self, a, b):
        return a > b 
    
    def clean(self, x):
        return len(x)



class TaskForm(forms.ModelForm):
    types=forms.ModelMultipleChoiceField(queryset=get_type_query_set(), widget=forms.SelectMultiple(attrs={'class':'form-control form-control-custom'}))
    summary = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), validators=[TextFieldMinLengthValidator(limit_value=4, message='количество символов должно превышать 4')])
    description = forms.CharField(widget=CKEditorWidget(), validators=[TextFieldMaxLengthValidator(100, 'Количество символов превышает 100 символов')])
    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'types')
        widgets = {
            'status':forms.Select(attrs={'class':'form-control form-control-custom'}),
        }