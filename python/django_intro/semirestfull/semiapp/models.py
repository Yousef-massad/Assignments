from django.db import models
from datetime import datetime

# Create your models here.
class ShowManager(models.Manager):
    def show_validations(self, postData):
        errors = {}
        
        if len(postData['title']) < 2 :
            errors['title'] = "title must be at least 2 characters"
            
        if len(postData['network']) < 3:
            errors['network'] = "network must be at least 3 characters"
            
        if len(postData['description']) > 0 and len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters if provided."
        
        if not postData.get('release_date'):
            errors["release_date"] = "Release date is required."
        else:
            release_date = datetime.strptime(postData['release_date'], '%Y-%m-%d').date()
            if release_date > datetime.today().date():
                errors["release_date"] = "Release date should be in the past."
                
        return errors
            
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)    
    objects = ShowManager()
    
        
        