from django.urls import path
from . import views
urlpatterns = [
    path('', views.store, name='home'),
    path('contact-us/', views.contactus, name='contact-us'),
    path('about-us/', views.about, name='about-us'),
    path('product/<str:id>', views.productInfo, name='product_info'),
    

]