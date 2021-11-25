#from os import PRIO_USER
from django.shortcuts import render
import pandas as pd
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Spreadsheet
from .forms  import Search
import json

# Create your views here.
def home_view(request):
    form = Search(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'spreadsheets/home.html', context)


class UploadTemplateView(TemplateView):
    template_name = 'spreadsheets/home.html'

def file_upload_view(request):
    print("foi enviado")
    
    if request.method == 'POST':
       
        try:
            xsl_file = request.FILES.get('file')
            obj = Spreadsheet.objects.create(file_name=xsl_file, xsl_file= xsl_file)
            obj.save()
            reader = pd.read_excel(xsl_file)
            print("TIPOOOOO!!!!!!")
            print("______________________________________")
            print(type(reader))
            readerhtml = reader.to_html
            print("Planilha!!!!!!")
            print("______________________________________")
            #print(readerhtml)
            """
            print("COLUNAS!!!!!!")
            print("______________________________________")
            column_names = list(reader.columns)
            print(column_names)
            """
            """
            print("Retirando um coluna!!!!!!")
            print("______________________________________")
            newreader = reader.drop('Hora de início', axis=1)
            #planilhaNova = planilha.drop('Hora de conclusão', axis=1)
            #planilhaNova = planilha.drop('Email', axis=1)   
            #planilhaNova = planilha.drop('Nome', axis=1)    
            print(newreader)

            print("Informaçoes da Tabela!!!!!!")
            print("______________________________________")
            print(newreader.info())

            #descrevendo mínimo e máximo das contagens
            print("descrevendo mínimo e máximo das contagens!!!!!!")
            print("______________________________________")
            print(newreader.describe().round(2))

            print("Separando por categoria!!!!!!")
            print("______________________________________")
            qtde_categoria = newreader['SEXO'].value_counts()
            print(qtde_categoria)

            qtde_categoria_perc = newreader['SEXO'].value_counts(normalize=True)
            print(qtde_categoria_perc)"""
            context = {
            'readerhtml' : readerhtml 
            }
            return render(request, 'spreadsheets/home.html', context)
            #return HttpResponse(readerhtml) 
        except:
            print('ERRO!!!!')
    return False

"""
def column_names():
    reader =  file_upload_view()
    columns = list(reader.columns)
    print("COLUNAS!!!!!!")
    print("__________________________________")
    print(columns)
    return columns

"""

"""
def getColumnNames(request):
    print("ENTROU NA FUNC")
    try:
        if request.method == "POST":
            reader =  file_upload_view()
            column_names = list(reader.columns)
            print("COLUNAS!!!!!!")
            print("__________________________________")
            print(column_names)
            algo = json.dumps(column_names)
            return HttpResponse(algo)

        else:
            return HttpResponse("vish deu ruim")
    except:
        print("erro except")
        return HttpResponse("erro except return ")

"""