from django.db import models

# Create your models here.
class books(models.Model):
    title = models.CharField(max_length=100)  # Title of the book (up to 100 characters)
    author = models.CharField(max_length=100)  # Author's name
    published_date = models.DateField()  # Publication date of the book

    def __str__(self):
        return f"{self.title} by {self.author}"    

class author(models.Model):
    first_name = models.CharField(max_length=50)  # first name
    last_name = models.CharField(max_length=50)  # last name
    birthdate = models.DateField()  # Publication date of the book

    def __str__(self):
        return f"{self.first_name} by {self.last_name}"
    

