from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self, postData):
        errors = {}
        
        name = postData.get('coursename' , '')
        description = postData.get('description' , '')
        
        if len(name) < 5:
            errors['name'] = "name must be at least 5 characters"
            
        if len(description) < 15:
            errors['description'] = "description must be at least 15 characters"  
            
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    objects = CourseManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)