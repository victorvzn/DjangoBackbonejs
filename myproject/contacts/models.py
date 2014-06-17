from django.db import models

# Create your models here.
class Contact(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name,)