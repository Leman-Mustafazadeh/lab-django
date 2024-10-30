from django.shortcuts import render

from django.http import HttpResponse,HttpResponseNotFound
def main(request):
    return HttpResponse("<h1>Esas sehife</h1>")

def about(request):
    return HttpResponse("<h2>Sayt haqqinda</h2>")

def contact(request):
    return HttpResponse("<h2>elaqe</h2>")

def archive(request,year):
    return HttpResponse(f'<h2>Arxivb</h2><p>{year}</p>')


def user(request,username="Undefined",age=0):
    return HttpResponse(f'<h2>Username -- {username} Age -- {age}</h2>')

def categories(request,name,age):
    return HttpResponse(f"""
                        <h2>Kateqoiya</h2>
                        <p>{name}</p>
                        <p>{age}</p>
                        """)
   
def pageNotFound(request,exception):
        return HttpResponseNotFound('<h1>Sehife tapilmadi</h1>')

