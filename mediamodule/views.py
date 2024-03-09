from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import UploadedFile

# Create your views here.


def upload_file(request):
    if request.method == 'POST':
        my_file = request.FILES['myfile']
        uploaded_file = UploadedFile(file=my_file)
        uploaded_file.save()
        return HttpResponseRedirect(reverse('get-cars'))
