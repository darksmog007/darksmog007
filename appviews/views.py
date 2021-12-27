import os
import json
from rest_framework.views import APIView
from django.http import HttpResponse
from appmodels import models
from appserializer import serializers


class SignUP(APIView):
    def post(self, request):
        """ request data to be accept -> endpoint /signup/
        {
            "age": 10,
            "name": "sud",
            "address": "bharub",
            "username": "sud",
            "password": "sud"
        }
        """
        try:
            requestdata = json.loads(request.body.decode("utf-8"))
            if "@" not in requestdata["username"]:
                return HttpResponse(json.dumps({"status":505, "msg": "username not correct"}))
            models.UserRegistration(name = requestdata["name"], age = requestdata["age"],
                         address = requestdata["address"], username = requestdata["username"],
                         password = requestdata["password"]).save()
            return HttpResponse(json.dumps({"status":200, "msg": "user created success"}))
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({"status":505, "msg": "something went wrong"}))


class LogIN(APIView):
    def post(self, request):
        """ request data to be accept -> -> endpoint /login/
        {
            "username": "sud",
            "password": "sud"
        }
        """
        try:
            requestdata = json.loads(request.body.decode("utf-8"))
            logvalidate = models.UserRegistration.objects.filter(username=requestdata["username"], password=requestdata["password"])
            if logvalidate:
                userdata = serializers.UserSerializer(logvalidate, many=True)
                udata = json.loads(json.dumps(userdata.data))[0]
                return HttpResponse(json.dumps({"status":200, "msg": "login success", "user_data": udata}))
            else:
                return HttpResponse(json.dumps({"status":505, "msg": "login not success, check your details"}))
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({"status":505, "msg": "something went wrong"}))


class ResetPassword(APIView):
    def post(self, request):
        """ request data to be accept -> endpoint /resetpassword/
        {
            "username": "sud",
            "password": "sud",
            "newpassword": "sud11"
        }
        """
        try:
            requestdata = json.loads(request.body.decode("utf-8"))
            logvalidate = models.UserRegistration.objects.filter(username=requestdata["username"], password=requestdata["password"])
            if logvalidate:
                models.UserRegistration.objects.filter(username=requestdata["username"], password=requestdata["password"]).update(password=requestdata["newpassword"])
                return HttpResponse(json.dumps({"status":200, "msg": "user data updated success"}))
            else:
                return HttpResponse(json.dumps({"status":505, "msg": "user not found"}))
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({"status":505, "msg": "something went wrong"}))