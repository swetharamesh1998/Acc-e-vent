from django.db import models

# Create your models here.
class LocTags(models.Model):
    tagname = models.CharField( max_length=50, primary_key= True)
 
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("_detail", kwargs={"pk": self.pk})

class PartTags(models.Model):
    tagname = models.CharField( max_length=50, primary_key= True)
 
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("_detail", kwargs={"pk": self.pk})








class Users(models.Model):

    uid = models.CharField(max_length=8,primary_key=True)
    tags = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("_detail", kwargs={"pk": self.pk})

class Locations(models.Model):

    locname = models.CharField(max_length=50,primary_key=True)
    tags = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("_detail", kwargs={"pk": self.pk})