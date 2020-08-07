from django.db import models

# Create your models here.
class Fossil(models.Model):
    name = models.CharField(max_length=200)    
    classification = models.CharField(max_length=200)
    width = models.FloatField()
    height = models.FloatField()
    photo = models.ImageField(upload_to='assets/fossils')

    def __str__(self):
        return self.name


class Mineral(models.Model):
    name = models.CharField(max_length=200)
    classification = models.CharField(max_length=200)
    width = models.FloatField()
    height = models.FloatField()
    photo = models.ImageField(upload_to='assets/minerals')

    def __str__(self):
        return self.name


class Rock(models.Model):
    name = models.CharField(max_length=200)
    classification = models.CharField(max_length=200)
    width = models.FloatField()
    height = models.FloatField()
    photo = models.ImageField(upload_to='assets/rocks')

    def __str__(self):
        return self.name


class Meteor(models.Model):
    name = models.CharField(max_length=200)
    classification = models.CharField(max_length=200)
    width = models.FloatField()
    height = models.FloatField()
    photo = models.ImageField(upload_to='assets/meteors')

    def __str__(self):
        return self.name