from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
import random

def home(request):                                   #장고에서 지원하는 request에 담아서 쏴주는 것(보여주는 것)
    return HttpResponse('<h1>WELCOME HOME!!!</h1>')    #브라우저에 통신할 가능성이 많아진다. request값을

class HomeView(View):           #class는 view를 상속받는 것
    def get(self, request, *args, **kwargs):
        #number = str(random.randint(100,1000))
        #return HttpResponse('<h1>WELCOMES CLASS HOME ['+number+']!!!!</h1>')
        # text = '<h1>안녕하세요</h1>'
        # text +='<h3>랜덤숫자'+number+'</h3>'
        # return HttpResponse(text)
        number = str(random.randint(10,80))         #randint:범위

        context = {
            "name" : "John",
            "number" : number,
            "present" : "<ul><li>내용1</li><li>내용2</li><li>내용3</li></ul>"
        }

        return render(request, "home.html", context)