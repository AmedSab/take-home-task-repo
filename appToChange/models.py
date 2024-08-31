from django.db import models

# Create your models here.

class MyChangingModel(models.Model):
    main_IntegerField = models.IntegerField()
    main_CharField = models.CharField(max_length=255, blank=True, default='', null=True)
    main_BooleanField = models.BooleanField(default=True)
    
    merge_conflict_EmailField = models.EmailField(max_length=255, blank=True, null=True)
    
    notMain_IntegerField = models.IntegerField()
    