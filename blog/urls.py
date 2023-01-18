from blog.views.account.register_view import (
    UserRegisterView, AccountActivationSentView, ActivateView)
from blog.views.account.logout_view import UserLogoutView
from blog.views.account.login_view import UserLoginView
from django.urls import path


# Specifies the app name for name spacing
app_name = "blog"

urlpatterns = [

    # ACCOUNT URLS
    # for register
    path('account/register/', UserRegisterView().as_view(), name='register'),
    # for login
    path('account/login/', UserLoginView.as_view(), name='login'),
    # for logout
    path('account/logout/', UserLogoutView.as_view(), name='logout'),
    # for account activation sent
    path('account_activation_sent/', AccountActivationSentView.as_view(),
         name='account_activation_sent'),
    # for account activate
    path('activate/<uidb64>/token/', ActivateView.as_view(), name='activate')


    # DASHBOARD URLS

]
