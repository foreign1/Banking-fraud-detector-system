from django import forms

class UploadDataForm(forms.Form):
    fraud_data = forms.FileField( allow_empty_file=False)