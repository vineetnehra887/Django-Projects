from django.shortcuts import render, HttpResponse

from .forms import MyfileUploadForm
from .models import file_upload




def index(request):
    if request.method == 'POST':
        form = MyfileUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            name = form.cleaned_data['file_name']
            the_files = form.cleaned_data['files_data']

            file_upload(file_name=name, my_file=the_files).save()
            
            return HttpResponse("file upload")
        else:
            return HttpResponse('error')

    else:
        
        context = {
            'form':MyfileUploadForm()
        }      
        
        return render(request, 'intex.html', context)
        



def show_file(request):
    all_data = file_upload.objects.all()

    context = {
        'data':all_data 
        }

    return render(request, 'view.html', context)