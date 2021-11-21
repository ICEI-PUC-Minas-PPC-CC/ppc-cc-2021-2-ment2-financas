from django import forms
from .views import file_upload_view


#colunas criados para exemplo
colunmchoices = (
    ('#1', 'Estado civil'),
    ('#2', 'SEXO'),
    ('#3', 'Faixa etária'),
    ('#4', 'Você tem filhos?'),
)

def column_names():
    reader =  file_upload_view()
    columns = list(reader.columns)
    print("COLUNAS!!!!!!")
    print("__________________________________")
    print(columns)
    return columns
#escolhas = column_names()

graphicchoices = (
    ('1.', 'Gráfico de Barras'),
    ('2.', 'Gráfico de setores'),
    ('3.', 'Gráfico de Linhas'),
)

class Search(forms.Form):
    colunas = forms.ChoiceField(choices =  colunmchoices)
    graficos = forms.ChoiceField(choices = graphicchoices)
    