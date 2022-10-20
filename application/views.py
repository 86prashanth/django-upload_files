from http.client import HTTPResponse
from django.shortcuts import render
from .forms import Upload_form 
from django.http import HttpResponse
# Create your views here.
def Upload_file(request):
    if request.method == "POST":
        form=Upload_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file and image saved sucessfully')
    else:
        form=Upload_form()
        context={
            'form':form,
                 }
    return render(request,'app/upload.html',context)

def upload_show(request):
    if request.method=='POST':
        form=Upload_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            img_object=form.instance
            return render(request,'app/upload_show.html',{'form':form,'img_obj':img_object})
    else:
        form=Upload_form()
        context={
            'form':form,
        }
    return render(request,'app/upload_show.html',context)