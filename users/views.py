import json
from . import forms
from django.template import loader
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import UserRegistration
from . import serializer
from django.views.decorators.csrf import csrf_exempt


class HomePage(APIView):
    def get(self, request):
        context = {}
        context["form"] = forms.Loginform()
        template = loader.get_template('home.html')
        return HttpResponse(template.render(context, request))

    @csrf_exempt
    def post(self, request):
        requestdata = request.POST
        logvalidate = UserRegistration.objects.filter(username = requestdata["username"], password = requestdata["password"])
        if logvalidate:
            userdata = serializer.UserSerializer(logvalidate, many=True)
            template = loader.get_template('profile.html')
            context = json.loads(json.dumps(userdata.data))[0]
            print(context)
            print(type(context))
            return HttpResponse(template.render(context, request))
        else:
            context = {}
            context["form"] = forms.Loginform()
            context["status"] = "wrong login details"
            template = loader.get_template('home.html')
            return HttpResponse(template.render(context, request))



class Login(APIView):
    def get(self, request):
        print("111")
        context = {}
        context["form"] = forms.Loginform()
        template = loader.get_template('login.html')
        return HttpResponse(template.render(context, request))

class SignUP(APIView):
    def get(self, request):
        context = {}
        context["form"] = forms.Signupform()
        template = loader.get_template('signup.html')
        return HttpResponse(template.render(context, request))

    @csrf_exempt
    def post(self, request):
        requestdata = request.POST
        UserRegistration(name = requestdata["name"], age = requestdata["age"],
                         address = requestdata["address"], username = requestdata["username"],
                         password = requestdata["password"]).save()
        template = loader.get_template('signup.html')
        return HttpResponse(template.render({"status": "user created success"}, request))


class Loginvalidate(APIView):
    def post(self, request):
        print("oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
        requestdata = request.POST
        print("===", requestdata)
        logvalidate = UserRegistration.objects.filter(username=requestdata["username"],
                                                      password=requestdata["password"])
        print("---", logvalidate)
        if logvalidate:
            # print(logvalidate["name"])
            template = loader.get_template('profile.html')
            return HttpResponse(template.render({"name": requestdata["username"]}, request))
        else:
            template = loader.get_template('login.html')
            return HttpResponse(template.render({"status": "wrong login details"}, request))
