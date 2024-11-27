from django.shortcuts import render
# from datetime from datetime
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound

# class MyClass:
#     def_init_(self,a,b):
#         self.a=a
#         self.b=b

# def index4(request):
#          return render(request,"limon/index4.html",context="my_date",datetime.now())


def index1(request):
    
    data = {"n": 5}
    return render(request, "index1.html", context=data)


def main(request):
    return HttpResponse("<h1>Esas sehife</h1>")


def about(request):
    return render(request,"limon/about.html")


def contact(request):
    return HttpResponse("<h2>elaqe</h2>")


def archive(request, year):
    return HttpResponse(f'<h2>Arxivb</h2><p>{year}</p>')


def user(request, username="Undefined", age=0):
    return HttpResponse(f'<h2>Username -- {username} Age -- {age}</h2>')


def categories(request, name, age):
    return HttpResponse(f"""
                        <h2>Kateqoiya</h2>
                        <p>{name}</p>
                        <p>{age}</p>
                        """)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Sehife tapilmadi</h1>')
