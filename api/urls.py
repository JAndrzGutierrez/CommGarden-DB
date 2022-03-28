from django.urls import path

from .views.user import SignUp, SignIn, SignOut, ChangePassword
from api.views.garden_tasks import Garden_TasksView


urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('garden_tasks/', Garden_TasksView.as_view(), name='garden_tasks'),

]