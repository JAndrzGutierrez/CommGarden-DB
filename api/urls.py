from django.urls import path
from .views.user import SignUp, SignIn, SignOut, ChangePassword
from api.views.garden_tasks import Garden_TasksView, Garden_TaskView


urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('garden_tasks/', Garden_TasksView.as_view(), name='garden_tasks'),
    path('garden_tasks/<int:pk>', Garden_TaskView.as_view(), name='garden_task'),
    
]