from django.urls import path
from blog import views

urlpatterns = [
    path('', views.BlogsView.as_view(), name='blogs'),
    path('about/', views.AboutView.as_view(), name='blog-about'),
    path('single-blog/<slug:slug>/', views.BlogDetailView.as_view(), name='single-blog'),
    path('like/<slug:slug>/', views.like, name='like_blog'),
]