from django.urls import path
from account.views import home, login_view, register_view,  password_reset_view, logout_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
#     path('activate/<str:uidb64>/<str:token>/',
#          activate_account, name='activate'),
    path('password_reset/', password_reset_view, name='password_reset'),
#     path('password_reset_confirm/<uidb64>/<token>/', password_reset_confirm_view,
#          name='password_reset_confirm'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', logout_view, name='logout' )
]
