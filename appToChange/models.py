from django.db import models
import uuid

# Create your models here.

class MyChangingModel(models.Model):
    main_IntegerField = models.IntegerField()
    main_CharField = models.CharField(max_length=255, blank=True, default='', null=True)
    main_BooleanField = models.BooleanField(default=True)
    main_EmailField = models.EmailField(max_length=255, blank=True, null=True)
    