from django.db import models
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your models here.
class Spreadsheet(models.Model):
    file_name = models.CharField(max_length=120, null=True)
    xsl_file = models.FileField(upload_to='spreadsheets_files', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name)