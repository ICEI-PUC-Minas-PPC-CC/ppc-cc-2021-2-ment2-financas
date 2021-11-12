from django.shortcuts import render
import pandas as pd
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Spreadsheet

# Create your views here.
def home_view(request):
    return render(request, 'spreadsheets/home.html', {})


class UploadTemplateView(TemplateView):
    template_name = 'spreadsheets/home.html'

def file_upload_view(request):
    print("foi enviado")
    
    if request.method == 'POST':
        xsl_file = request.FILES.get('file')
        obj = Spreadsheet.objects.create(file_name=xsl_file)
        obj.save()
    """
        with open(obj.file_name.path, 'r') as f:
            reader = pd.read_excel(f) 
            for row in reader:
               print(row, type(row)) """
    return HttpResponse()