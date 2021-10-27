from django.urls import path
from django.views.generic import TemplateView
from users.views import UserDetailView ,user_login, user_logout, user_signup, update_profile

urlpatterns=[
    path(
        route='login/', 
        view=user_login, 
        name='login'
        ),
    path(
        route='logout/', 
        view=user_logout, 
        name='logout'
        ),
    path(
        route='signup/', 
        view=user_signup, 
        name='signup'),
    path(
        route='profile/update', 
        view=update_profile, 
        name='update_profile'
        ),
    path(
        route='<str:username>/',
        view=UserDetailView.as_view(),
        name='profile'
    )
]