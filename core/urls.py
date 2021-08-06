from django.urls import path
from core import views

urlpatterns = [ 
    path('error-404/', views.ErrorView.as_view(), name='error-404'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='core-contact'),
]
