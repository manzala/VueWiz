from django.db import models

class uploadModel(models.Model):
    pdfFile = models.FileField(upload_to = '/media')
