from django.shortcuts import render
from testapp.models import resume,personal_info,career_info,exam_info
from testapp.forms import ResumeForm,Personal_info_Form,Career_info_Form,Exam_info_Form

# Create your views here.
def home(request):
    return render(request,'testapp/home.html')
def show_resume(request):
    return render(request,'testapp/simpleresume.html')
def resumeform_view(request):
    resumeform=ResumeForm(request.POST)
    return render(request,'testapp/resumeform.html',{'resumeform':resumeform})
