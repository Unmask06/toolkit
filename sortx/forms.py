from django import forms

class SortxForm(forms.Form):
    config_path = forms.CharField(label="Configuration Path", max_length=300)
    xl_folder_path = forms.CharField(label="Excel Folder Path", max_length=300, required=False)
    doc_folder_path = forms.CharField(label="Documents Folder Path", max_length=300, required=False)