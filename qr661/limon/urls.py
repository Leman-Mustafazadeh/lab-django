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
    re_path(r'^archive/(?P<year>\d{4})/$', views.archive, name='archive'),
    re_path(r'^user/(?P<username>\w+)/(?P<age>\d+)/$', views.user, name='user_with_age'),
    re_path(r'^user/(?P<username>\w+)/$', views.user, name='user'),
    re_path(r'^user/$', views.user, name='user_list'),
    path('category/', views.categories, kwargs={"name": "laman", "age": 21}, name='categories'),
]

