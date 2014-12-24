from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Twitter(models.Model):
    text = models.CharField(max_length=50)
    name = models.ForeignKey(User)
    def __unicode__(self):
        return self.text



