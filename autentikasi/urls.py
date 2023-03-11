from django.urls import path

from .views import signup,login_user,logout_user,get_session_id,get_username
urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/',signup, name='signup'),
    path('getUsername/',get_username,name= "get-username"),
    path('sesi/',get_session_id,name="sessionId")
]