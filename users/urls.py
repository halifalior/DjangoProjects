from django.conf.urls import url , include
from users.views import home , register

urlpatterns = [
    url('accounts/',include("django.contrib.auth.urls")),
    url('register/', register, name="register"),
    url('', home, name="home"),
]

