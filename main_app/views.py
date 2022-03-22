from distutils.log import error
from django.shortcuts import redirect, render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from main_app.forms import GigForm
from .models import Band, Gig, Venue


#===================================
#        TEST VIEWS
#===================================
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse('<h1>Hello World</h1>')

# def about(request):
#     return HttpResponse('<h1>About Gig App</h1>') 


#===================================
#        SIGNUP VIEW
#===================================   
def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes that data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or GET request, so render signup.html 
    #  with an empty form     
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)     

#===================================
#        BAND VIEWS
#===================================
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')    

# This is the def function way of creating the index view
@login_required
def bands_index(request):
    bands = Band.objects.filter(user=request.user)
    # You could also code it this way
    # bands = request.user.band_set.all()
    return render(request, 'bands/index.html', {'bands': bands})

# This is the ListView way of creating the index view
# class BandList(ListView):
#     model = Band 
#     template_name = 'bands/index.html'

# pk - is the primary key of the band from BandList
@login_required
def bands_detail(request, pk):
    band = Band.objects.get(id=pk)
    gig_form = GigForm()
    return render(request, 'bands/details.html', {
        'band': band,
        'gig_form': gig_form
        })

def add_gig(request, band_id):
    form = GigForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db unit it
        # has the band_id assigned to it
        new_gig = form.save(commit=False)
        # commit=False will create an in-memory object
        # so that we can assign the band_id before
        # really saving to the db
        new_gig.band_id = band_id
        new_gig.save()
    return redirect('detail', pk = band_id)    

def delete_gig(request, band_id, gig_id):
    # create a dictionary for intial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Gig, id = gig_id)

    if request.method == 'POST':
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return redirect('detail', pk = band_id)   

    return render(request, 'main_app/gig_confirm_delete.html', context)    

class BandCreate(LoginRequiredMixin, CreateView):    
    model = Band
    fields = ['band_name','mgr_name','mgr_email','mgr_phone']
    # This Django inherited method is called when a
    # valid band form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user # form.intance is the band
        return super().form_valid(form) 
        # super(). is a way of calling a parent function - even outside of the function

class BandUpdate(LoginRequiredMixin, UpdateView):    
    model = Band
    fields = ('__all__')

class BandDelete(LoginRequiredMixin, DeleteView):    
    model = Band
    # Have to use the success_url attribute
    #  to return to the index page
    #  with the DeleteView, because no details instance to return to
    success_url = '/bands/'
    

#========================
#     VENUE VIEWS
#========================

def venues_index(request):
    venues = Venue.objects.all()
    return render(request, 'venues/index.html', {'venues': venues})

def venues_detail(request, pk):
    venue = Venue.objects.get(id=pk)
    return render(request, 'venues/detail.html', { 'venue': venue })

class VenueCreate(LoginRequiredMixin, CreateView):
    model = Venue
    fields = '__all__'
    # success_url = '/venues/'

class VenueUpdate(LoginRequiredMixin, UpdateView):
  model = Venue
  fields = '__all__'

class VenueDelete(LoginRequiredMixin, DeleteView):
  model = Venue
  success_url = '/venues/'