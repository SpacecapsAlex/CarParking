from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import UploadedFile

# Create your views here.


def upload_file(request):
    print(f'upload file {request}')
    if request.method == 'POST':
        print('upload file')
        print(f'files - {request.FILES}')
        my_file = request.FILES['myfile']
        print(f'file - {my_file}')
        uploaded_file = UploadedFile(file=my_file)
        print(f'file object - {uploaded_file}')
        uploaded_file.save()
        print('file saved')
        return HttpResponseRedirect(reverse('get-cars'))
