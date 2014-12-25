from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Twitter(models.Model):
    text = models.CharField(max_length=50)
    name = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.text



