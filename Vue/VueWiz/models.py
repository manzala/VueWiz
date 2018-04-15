from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class uploadModel(models.Model):
    title = models.CharField(db_column='title', max_length=180, blank=True, null=True, help_text="Title of the image") 
    pdfFile = models.FileField(db_column='pdffile', upload_to='media', null=True, blank=True, help_text="Load a pdf.")
  
    class Meta:
        managed = True
