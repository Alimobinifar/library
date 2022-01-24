from django.db import models

# Create your models here.


class Publisher(models.Model):
    name=models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Category(models.Model):
    category=models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Author(models.Model):
    author=models.CharField(max_length=100)
    def __str__(self):
        return  self.author


class Book(models.Model):
    name=models.CharField(max_length=200)
    pages=models.CharField(max_length=200)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    price=models.IntegerField()
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='images/')
    publisher=models.ForeignKey(Publisher,on_delete=models.PROTECT)
    def __str__(self):
        return self.name





