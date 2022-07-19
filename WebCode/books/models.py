from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Book(models.Model):
    category_choices =(
        #("Undefined","Undefined"),
        ("Action", "Action"),
        ("Romance", "Romance"),
        ("Horror", "Horror"),
        ("Comedy", "Comedy"),
        ("Adventure", "Adventure"),
        ("Dramatic", "Dramatic"),
        ("Crime","Crime"),
        ("Fantasy","Fantasy"),
    )
    
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True)
    content = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to= 'photos/%y/%m/%d', blank = True)
    category = models.CharField(
        max_length = 20,
        choices = category_choices,
        )
    publication_year = models.CharField(max_length=4, null=True)
    ISBN = models.CharField(max_length=13, null=True, unique=True)
    active = models.BooleanField(default= True)

    def __str__(self):
        return self.name

class Borrow(models.Model):
    name = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='Borrow A Book')
    book = models.OneToOneField(Book, null=True, on_delete= models.SET_NULL)
    period = models.PositiveIntegerField(default=0)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.book)
