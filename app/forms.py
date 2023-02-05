from django import forms

def validate_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('name is started with a')

def check_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('len is too low')
class NameForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[validate_for_a,check_for_len])
    age=forms.IntegerField()
    email=forms.EmailField(max_length=100)
    remail=forms.EmailField(max_length=100)
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
def clean(self):
    e=self.cleaned_data['email']
    r=self.cleaned_data['remail']
    if e!=r:
        raise forms.ValidationError('not matched')