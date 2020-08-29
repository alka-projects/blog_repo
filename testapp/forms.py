from django import forms
from testapp.models import resume,personal_info,career_info,exam_info



class ResumeForm(forms.ModelForm):
    class Meta:
        model= resume
        fields= '__all__'

class Personal_info_Form(forms.ModelForm):
    class Meta:
        model= personal_info
        fields= '__all__'

class Career_info_Form(forms.ModelForm):
    class Meta:
        model= personal_info
        fields= '__all__'

class Exam_info_Form(forms.ModelForm):
    class Meta:
        model= personal_info
        fields= '__all__'