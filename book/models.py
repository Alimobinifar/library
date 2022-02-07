from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):

    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author


class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.IntegerField()
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    img = models.ImageField(upload_to='images/', null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
