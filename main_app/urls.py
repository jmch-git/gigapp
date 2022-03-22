from django.urls import path
from . import views


   # This is the ListView way of defining a url path
   #path('bands/', views.BandList.as_view(), name='index'),

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('bands/', views.bands_index, name='index'),
   path('bands/<int:pk>/', views.bands_detail, name='detail'),
   path('bands/create/', views.BandCreate.as_view(), name='bands_create'),
   path('bands/<int:pk>/update', views.BandUpdate.as_view(), name='bands_update'),
   path('bands/<int:pk>/delete', views.BandDelete.as_view(), name='bands_delete'),
   path('bands/<int:band_id>/add_gig/', views.add_gig, name='add_gig'),
   path('bands/<int:band_id>/delete_gig/<int:gig_id>', views.delete_gig, name='delete_gig'),
   path("venues/", views.venues_index, name="venues_index"),
   path("venues/<int:pk>/", views.venues_detail, name="venues_detail"),
   path("venues/create/", views.VenueCreate.as_view(), name='venues_create'),
   path("venues/<int:pk>/update/", views.VenueUpdate.as_view(), name="venues_update"),
   path("venues/<int:pk>/delete/", views.VenueDelete.as_view(), name="venues_delete"),
   path('accounts/signup/', views.signup, name='signup'),
]
