from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        
        errors = {}
        
        first_name = postData['first_name']
        last_name = postData['last_name']
        email = postData['email']
        password = postData['password']
        confirm_password = postData['confirm_password']
        
        if len(first_name) < 2:
            errors["first_name"] = "First name must be at least 2 characters."

        elif not first_name.isalpha():
            errors["first_name"] = "First name must contain letters only."

        if len(last_name) < 2:
            errors["last_name"] = "Last name must be at least 2 characters."

        elif not last_name.isalpha():
            errors["last_name"] = "Last name must contain letters only."

        EMAIL_REGEX = re.compile(
            r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        )

        if not EMAIL_REGEX.match(email):
            errors["email"] = "Please enter a valid email address."

        elif User.objects.filter(email__iexact=email).exists():
            errors["email"] = "Email is already registered."

        if len(password) < 8:
            errors["password"] = "Password must be at least 8 characters."

        if password != confirm_password:
            errors["confirm_password"] = "Passwords do not match."

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    objects = UserManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
