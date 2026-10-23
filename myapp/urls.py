
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('error/', views.error, name='error'),
    path('blog-details.html', views.details, name='details'),
    path('blog.html', views.blog, name='blog'),
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('service/', views.service, name='service'),
    path('starter/', views.starter, name='starter'),
    path('show/', views.show, name='show'),

]
