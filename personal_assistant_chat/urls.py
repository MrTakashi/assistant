from django.urls import path
from personal_assistant_chat import views

urlpatterns = [
    path("", views.home, name="home"),
    path("1", views.chat_no_design, name="chat_no_design"),
]