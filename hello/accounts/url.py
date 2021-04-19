from django.contrib import admin


# from accounts.views import login_view, logout_view
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from accounts.views import register_view, UserDetailView

app_name = 'account'
urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/login', login_view, name='login'),
    # path('accounts/logout/', logout_view(), name='logout')
    path('accounts/login', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('create/', register_view, name = 'create'),
    path('detail/<int:pk>', UserDetailView.as_view(), name = 'detail')




]
