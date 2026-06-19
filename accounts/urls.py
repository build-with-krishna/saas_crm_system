from django.urls import path
from .views import company_signup,user_login,user_logout

urlpatterns = [

    path('signup/', company_signup, name='signup'),

    path('login/', user_login, name='login'),

    path('logout/', user_logout, name='logout'),

]