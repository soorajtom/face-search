from django.db import models
from django.db.models.fields import DateTimeField
from django.utils.safestring import mark_safe
import datetime

class File(models.Model):
    '''
        Store face image entry. 
    '''
    # Path to the image file.
    filepath = models.CharField(max_length=255)
    
    # Date of ingestion.
    date_added = models.DateField(default=datetime.date.today)

    # Date of file creation.
    date_created = models.DateField(default=datetime.date.today)
    
    # Face vectors from DLib.
    vector = models.TextField(null=True)
