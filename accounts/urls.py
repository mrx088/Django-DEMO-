from django.urls import path
from . import views
from rest_framework.authtoken import views as TokenView

app_name = 'accounts'
urlpatterns = [
    path('users/', views.AllUsers.as_view(),name='all_user'),
    path('register/',views.RegisterUser.as_view(),name='register_user'),
    path('api-token-auth/', TokenView.obtain_auth_token),
    path('questions/', views.AllQuestion.as_view(),name="user_questions"),
    path('question/create/', views.CreateQuestion.as_view(),name="create_questions"),
    path('question/update/<int:pk>', views.UpdateQuestion.as_view(),name="update_questions"),
    path('question/delete/<int:pk>', views.DeleteQuestion.as_view(),name="delete_questions"),






]
