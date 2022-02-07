from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    stack = models.CharField(max_length=60, null=True, blank=True)
    images = models.ImageField(null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    telegram = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Courses(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    number_les = models.IntegerField()
    davomiyligi = models.CharField()
    price = models.CharField(max_length=50, null=True, blank=True)
    image_cours = models.FileField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self) -> str:
    #     return self.name

class Post(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self) -> str:
        # return self.title

class Galereya(models.Model):
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    image4 = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.created


class Contact(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self) -> str:
    #     return self.name