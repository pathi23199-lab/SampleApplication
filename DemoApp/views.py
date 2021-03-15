from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from .models import User_Json
from .forms import User_JsonForm
import json
# from somewhere import handle_uploaded_file

@login_required
def myView(request):
    form=forms.User_JsonForm()

    return render(request,'DemoApp/home.html',{'form':form})
def result(request):
    form = User_Json.objects.all()

    return render(request,'DemoApp/result.html',{'form':form})
# def logOut(request):
#     return render(request, 'DemoApp/logout.html')
# Create your views here.
def handle_uploaded_file(f):
    destination = open('media/upload/'+f.name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
def save_File(request):
    print(request.FILES)
    print("inside savefile")
    if request.method == 'POST':
        print("post savefile")
        form = User_JsonForm(request.POST, request.FILES)
        # print(form.)
        if form.is_valid():
            print(form.cleaned_data)
            # form = User_JsonForm(request.POST, request.FILES)
            file=request.FILES['docfile']
            handle_uploaded_file(file)
            with open('media/upload/'+file.name) as f:
                data = json.load(f)
                # print(data)
                for d1 in data:
                    p = User_Json.objects.get_or_create(userId=d1['userId'], ID=d1['id'],body=d1['body'],title=d1['title'])
                    # p.save(force_insert=True)
                        # form.cleaned_data['userId']=d1['userId']
                        # form.cleaned_data['ID'] = d1['id']
                        # form.cleaned_data['body'] = d1['body']
                        # form.cleaned_data['title'] =  d1['title']
                        # print(form.cleaned_data)
                        # print("copy----",form.body)
                        # form.save(commit=True)
                        # print("userId:",d1['userId'])
                        # print("Id:", d1['id'])
                        # print("Title:", d1['title'])
                        # print("Body:", d1['body'])
            # Output: {'name': 'Bob', 'languages': ['English', 'Fench']}

            # return HttpResponse("File uploaded successfuly")
            # file=request.FILES['myfile']
            # for dict in file:
            #    print(dict['userId'])
            # print("valid File")
            # form.docfile={"sdf":5445,"dfs":"sdfsdf"}
            # print(form.docfile)
            # form.save()

            return render(request, 'DemoApp/result.html')
        else:
            print("Not valid File")
            # form.save()
            # form = UploadFileForm()
    return render(request,'DemoApp/home.html')

