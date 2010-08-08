from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Device(models.Model):
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    owner = models.ForeignKey(Member)
    image_url = models.URLField(verify_exists=False, null=True, default='http://test.com/')

    def __unicode__(self):
        return self.description

