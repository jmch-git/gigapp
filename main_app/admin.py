from django.contrib import admin
from .models import Band, Venue, Gig

# Register your models here.
admin.site.register(Band)
admin.site.register(Gig)
admin.site.register(Venue)