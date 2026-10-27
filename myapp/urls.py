
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
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),

    #Mpesa urls
    
     path('pay/', views.pay, name='pay'),

    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('payment-result/', views.payment_result, name='payment_result'),
    path('transactions/', views.transactions_list, name='transactions'),


    

]
