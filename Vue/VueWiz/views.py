from django.shortcuts import render
from django.shortcuts import render
import os
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from forms import UserRegistrationForm
from django.http import HttpResponse
from models import VideoModel
from models import ResumeModel
from forms import uploadForm
from forms import videoForm
from django.conf import settings
from django.core.files.storage import default_storage



# Create your views here.
def index(request):
    return render(request, template_name="index.html", context={"done": True})

def done(request):
    return render(request, template_name="done.html", )

def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    resume = ResumeModel.objects.get(user=request.user)
    print(resume.id)
    return render(request, template_name="profile.html", context={"resume": resume})

# is protected by user login but needs to have user level premissions
def media(request, path):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    file_path = os.path.join(settings.MEDIA_ROOT, 'media', path)
    print('path: {}'.format(path))
    print('file_path: {}'.format(file_path))
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    return HttpResponseRedirect('/')

def error(request):
    return render(request, template_name="error.html")

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            print(userObj)
            email = userObj['email']
            password = userObj['password']
            if not (User.objects.filter(email=email).exists()):
                User.objects.create_user(username=email,email=email, password=password)
                user = authenticate(username=email,email=email,  password=password)
                # login(request,user)
                return HttpResponseRedirect('/done')
            else:
                return HttpResponseRedirect('/error')
                # raise forms.ValidationError('Looks like a username with that email or password already exists')
    return HttpResponseRedirect('/#contact')
    #     form = UserRegistrationForm()
    # return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            print(userObj)
            email = userObj['email']
            password = userObj['password']

            user = authenticate(username=email,email=email,  password=password)
            if(user):
                login(request, user)
                return HttpResponseRedirect('/upload')
        else:
            raise forms.ValidationError('Looks like BAD PASSWORD DUD')
    else:
        form = UserRegistrationForm()
    return render(request, 'signin.html', {'form': form})

def upload_resume(request):
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        print "Hi"
        if form.is_valid():
            userObj= form.cleaned_data
            print "hi"
            pdfFile= userObj['uploadField'] #looks at html name
            resumeModel = ResumeModel()
            resumeModel.user = request.user
            resumeModel.file = pdfFile
            resumeModel.save()
            return HttpResponseRedirect("/profile")
    return HttpResponseRedirect("/profile")

def upload_video(request):
    if request.method == 'POST':
        form = videoForm(request.POST, request.FILES)
        print "Hi"
        if form.is_valid():
            userObj= form.cleaned_data
            print "hi"
            videoFile= userObj['videoField'] #looks at html name
            introVideoModel = VideoModel()
            introVideoModel.user = request.user
            introVideoModel.file = videoFile
            ext = os.path.splitext(str(videoFile))
            if(ext is '.mp4' or ext is '.MP4'):
                introVideoModel.save()
                return HttpResponse('video upload success')
            else:
                return HttpResponse("This isnt mp4 DUFUS !")
    else:
        form = videoForm()
    return render(request, 'upload_video.html', {'form': form})
