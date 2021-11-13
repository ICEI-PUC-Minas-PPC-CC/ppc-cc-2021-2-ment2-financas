from django.shortcuts import render
import pandas as pd
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Spreadsheet
import openpyxl as xl

# Create your views here.
def home_view(request):
    return render(request, 'spreadsheets/home.html', {})


class UploadTemplateView(TemplateView):
    template_name = 'spreadsheets/home.html'

def file_upload_view(request):
    print("foi enviado")
    
    if request.method == 'POST':
        xsl_file = request.FILES.get('file')
        obj = Spreadsheet.objects.create(file_name=xsl_file, xsl_file= xsl_file)
        obj.save()
        #f = obj.file.open('r')
        #with open(obj.file_name, 'r') as f:
        #f = obj.file_name.open('r')
        reader = pd.read_excel(xsl_file)
        for row in reader:
            print(row, type(row))
    return HttpResponse()