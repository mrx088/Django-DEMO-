from django.urls import path
from . import views
from rest_framework.authtoken import views as TokenView

app_name = 'accounts'
urlpatterns = [
    path('users/', views.AllUsers.as_view(),name='all_user'),
    path('register/',views.RegisterUser.as_view(),name='register_user'),
    path('api-token-auth/', TokenView.obtain_auth_token),


]
