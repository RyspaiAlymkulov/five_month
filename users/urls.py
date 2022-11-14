from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.login_view),
    path('register/', views.register_view)
]