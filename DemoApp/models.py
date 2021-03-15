from django.db import models

# Create your models here.
class User_Json(models.Model):
    userId = models.CharField(max_length=30)
    ID = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    body = models.CharField("Address line 1",max_length=40000,)
    docfile = models.FileField(upload_to ='documents',blank=False)
    # file = forms.FileField()models.FileField(upload_to ='uploads/% Y/% m/% d/')