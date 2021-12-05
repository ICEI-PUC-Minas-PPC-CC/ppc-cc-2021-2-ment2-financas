from django.shortcuts import render
import pandas as pd
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Spreadsheet
from .forms  import Search
import json

# Create your views here.
def home_view(request):
    if request.method == 'POST':
        try:
            xsl_file = request.FILES.get('file')
            obj = Spreadsheet.objects.create(file_name=xsl_file, xsl_file=xsl_file)
            obj.save()
            reader = pd.read_excel(xsl_file)
            print(type(reader))
            readerhtml = reader.to_html
            #info = reader.info()
            describe = reader.describe().round(2).to_html
            print(type(describe))
            form = Search(request.POST or None)
            context = {
              'readerhtml': readerhtml,
              'describe': describe,
              'form': form,
            }
            return render(request, 'spreadsheets/home.html', context)
        except:
            print('ERRO!!!!')
            context = {
                'test': 'passou pelo try'
            }
            return render(request, 'spreadsheets/home.html', context)
    return render(request, 'spreadsheets/home.html')

class UploadTemplateView(TemplateView):
    template_name = 'spreadsheets/home.html'
