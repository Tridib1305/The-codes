from django import forms
from accounts.models import Lost_Object
class Lost_Object_New(forms.ModelForm):
    Product_Name=forms.CharField(max_length=50, required=True),
    Description=forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={
        "placeholder":"Description of your Product", 
    }))
    Image=forms.ImageField(required=False)
    class Meta:
        model=Lost_Object
        exclude=("Name_and_Roll_no_of_Person",)