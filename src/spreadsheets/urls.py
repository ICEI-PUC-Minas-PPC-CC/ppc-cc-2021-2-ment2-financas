from django.urls import path
from .views import (
    home_view,
    UploadTemplateView,
    
    )
#file_upload_view,
#getColumnNames,
app_name = 'spreadsheets'

urlpatterns = [
    path('', home_view, name='home'),    
    path('from_file/', UploadTemplateView.as_view(), name='from-file'),
    #path('upload/', file_upload_view, name='upload'),   
    #path('colunmns/', getColumnNames, name='colunmns'),   
]
