from django.db import models

# Create your models here.
class SchoolErp(models.Model):
    school_url = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    admin_username = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=100)