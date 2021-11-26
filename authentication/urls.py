from django.urls.conf import path
from authentication import controllers


urlpatterns = [
    path("login/", controllers.Login.as_view()),
    path("verify/", controllers.CreateUser.as_view())
]