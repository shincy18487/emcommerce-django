from django.urls import path
from . import views


urlpatterns=[

       path('register/',views.register,name='register'),
       path('login/',views.login,name='login'),
       path('logout/',views.logout,name='logout'),
       path('activate/<uidb64>/<token>/',views.activate,name='activate'),
       path('dashboard/',views.dashboard,name='dashboard'),
       path('',views.dashboard,name='dashboard'),
       path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
       path('password_validation/<uidb64>/<token>/',views.password_validation,name='password_validation'),
       path('resetPassword/',views.resetPassword,name='resetPassword')

      ]
