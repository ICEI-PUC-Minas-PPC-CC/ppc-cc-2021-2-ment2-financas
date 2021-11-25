from django import forms

#colunas criados para exemplo
colunmchoices = (
    ('#1', 'Estado civil'),
    ('#2', 'SEXO'),
    ('#3', 'Faixa etária'),
    ('#4', 'Você tem filhos?'),
)
""""
def column_names():
    from .views import file_upload_view  #<-------------
    reader =  file_upload_view()
    columns = list(reader.columns)
    print("COLUNAS!!!!!!")
    print("TIPOOOOO!!!!!!")
    print("______________________________________")
    print(type(reader))
    print("__________________________________")
    print(columns)
    return columns
        """
#escolhas = column_names()

graphicchoices = (
    ('1.', 'Gráfico de Barras'),
    ('2.', 'Gráfico de setores'),
    ('3.', 'Gráfico de Linhas'),
)

class Search(forms.Form):
    #escolhas = column_names()
    colunasX = forms.ChoiceField(choices =  colunmchoices)
    colunasY = forms.ChoiceField(choices =  colunmchoices)
    graficos = forms.ChoiceField(choices = graphicchoices)