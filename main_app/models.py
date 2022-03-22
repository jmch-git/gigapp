from random import choice
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# The User Model is imported here ^^ 
#  which by default has the following attributes:
#  username
#  password
#  email
#  first_name
#  last_name
# Some projects may need additional attributes, such as birthdate
#  If you need this functionality there are a few approaches - see further study on markdown


#====================================
#               MODELS
#====================================

class Band(models.Model):
    band_name = models.CharField(max_length=100)
    mgr_name = models.CharField(max_length=50)
    mgr_email = models.CharField(max_length=100)
    mgr_phone = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.band_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})


class Venue(models.Model):
    venue_name = models.CharField(max_length=100)
    # blank=True, null=True is so the field is not required
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    zip = models.CharField(max_length=15)
    phone = models.CharField(max_length=30)
    website = models.CharField(max_length=200)
    
    def __str__(self):
        return self.venue_name

    def get_absolute_url(self):
        return reverse('venues_detail', kwargs={'pk': self.id})
        

class Gig(models.Model):
    venues_list = Venue.objects.all()
    date = models.DateField('gig date')
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.date}{self.venue}'

    class Meta:
        ordering = ['date']    
