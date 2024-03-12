from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('users/', views.AllUsers.as_view(),name='all_user'),

]
