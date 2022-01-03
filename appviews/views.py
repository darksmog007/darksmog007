import os
import json
import datetime as dt
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
            "Phone": "",
            "pincode":"",
            "Gender":"",
            "Martialsts":"",
        }
        """
        try:
            requestdata = json.loads(request.body.decode("utf-8"))
            requestdata["userid"] = str(dt.datetime.now()).replace(":", "").replace("-", "").replace(" ", "").replace("_", "").replace(".","")
            if "@" not in requestdata["username"]:
                return HttpResponse(json.dumps({"status":505, "msg": "username not correct"}))
            dupcheck = models.UserRegistration.objects.filter(username=requestdata["username"])
            if dupcheck:
                return HttpResponse(json.dumps({"status":500, "msg": "username already exist"}))
            usr_serializer = serializers.UserSerializer(data=requestdata)
            if usr_serializer.is_valid():
                usr_serializer.save()
                return HttpResponse(json.dumps({"status":200, "msg": "user created success"}))
            else:
                return HttpResponse(json.dumps({"status": 505, "msg": "data not correct", "error": usr_serializer.errors}))
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

#########################################################################################################
class UserData(APIView):
    def get(self, request, pk):
        """
        method = get
        purpose: fetch data where userid = 20211230055322098852
        endpoint = /userdata/20211230055322098852
        where userid = 20211230055322098852
        """
        if pk:
            userdata = models.UserRegistration.objects.filter(userid=pk)
            userdata = serializers.UserSerializer(userdata, many=True)
            udata = json.loads(json.dumps(userdata.data))[0]
            return HttpResponse(json.dumps({"status": 200, "msg": "success", "udata": udata}))
        else:
            return HttpResponse(json.dumps({"status": 505, "msg": "something went wrong"}))

    def put(self, request, pk):
        """
        purpose : update the data which have userid = 20211230055322098852
        method = put
        endpoint = /userdata/20211230055322098852
        where userid = 20211230055322098852
        body json
        {
            "age": 10,
            "name": "sud",
            "address": "bharub",
            "username": "sud@mail.com",
            "password": "sud",
            "Phone": "1111111111",
            "pincode":"222222",
            "Gender":"M",
            "Martialsts":"F"
        }
        """
        requestdata = json.loads(request.body.decode("utf-8"))
        requestdata["userid"] = pk
        usrdata = models.UserRegistration.objects.filter(userid=pk).first()
        usr_serializer = serializers.UserSerializer(usrdata, data=requestdata)
        if usr_serializer.is_valid():
            usr_serializer.save()
            return HttpResponse(json.dumps({"status": 200, "msg": "updated sucess"}))
        else:
            return HttpResponse(json.dumps({"status": 505, "msg": "data not correct", "error": usr_serializer.errors}))

    def delete(self, request, pk):
        """
        method = delete
        purpose: delete data where userid = 20211230055322098852
        endpoint = /userdata/20211230055322098852
        where userid = 20211230055322098852
        """
        usrdata = models.UserRegistration.objects.filter(userid=pk)
        usrdata.delete()
        return HttpResponse(json.dumps({"status": 200, "msg": "deleted success"}))

##################################################################################################
class AllUserData(APIView):
    def get(self, request):
        """
        purpose: fetch all user data
        endpoint = /alluserdata/
        """
        userdata = models.UserRegistration.objects.all()
        userdata = serializers.UserSerializer(userdata, many=True)
        udata = json.loads(json.dumps(userdata.data))
        return HttpResponse(json.dumps({"status": 200, "msg": "success", "udata": udata}))