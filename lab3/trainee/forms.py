from django import forms
from .models import Trainee
class InsertForm(forms.Form):
    name=forms.CharField(max_length=20,label='Name',required=False)
    branch=forms.IntegerField(label='Branch')
    courses = forms.ChoiceField(choices=[(1, 'python'), (2, 'html'), (3, 'css'), (4, 'django')],label='Course')
    name.widget.attrs['class']='form-group'
    courses.widget.attrs['class']='form-group'
    branch.widget.attrs['class']='form-group'
    levels = forms.ChoiceField(choices=[(1,'python'),(2,'html')])