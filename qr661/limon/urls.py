from django.urls import path, re_path
from limon import views

# urlpatterns= [
#     path("haqqinda/",views.about),
#      path("elaqe/",views.contact)
# ]

urlpatterns = [
    path('', views.main, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
   
]

