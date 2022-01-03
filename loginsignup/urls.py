from django.contrib import admin
from django.urls import path
from appviews import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignUP.as_view(), name = "signup"),
    path('login/', views.LogIN.as_view(), name = "login"),
    path('resetpassword/', views.ResetPassword.as_view(), name = "resetpassword"),
    path('userdata/<str:pk>', views.UserData.as_view(), name = "userdata"),
    path('alluserdata/', views.AllUserData.as_view(), name = "alluserdata"),
]
