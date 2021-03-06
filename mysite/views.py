from django.http import HttpResponse
from django.views.generic import View       # generic:
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm        #form만드는 것 비디오 폼할 때도 넣었다.
from django.core.urlresolvers import reverse_lazy

#def home1(request):
#    text = "Hello World"
#    return HttpResponse(text)
#def about(request):
#    text ="<h1>우리에 대한 소개</h1>"
#    text +="좋은 회사입니다."
#    return HttpResponse(text)
#def team(request):
#    text = "<h1>팀장 : John</h1>"
#    text +="<h1>팀원 : Jane</h1>"
#    return HttpResponse(text)

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html", {})

class Base(View):
    def get(self, request, *args, **kwargs):
        return render(request, "base.html", {})

class Team(View):
    def get(self, request, *args, **kwargs):
        context = {
            "team" : "숭이",
            "number" : "10명",
        }
        return render(request, "team.html", context)

        # 함수 get방식을 쓰는 것
        # request의 텍스트 불러오기 {} : 서버에서 표시하고 싶은 값이 있을 때 쓰는 것
        # 클래스는 대문자, 함수는 소문자.

class Landingpage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "landingpage.html", {})

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneView(TemplateView):
    template_name = 'registration/register_done.html'
