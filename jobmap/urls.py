from django.urls import path
from . import views
from django.contrib.auth.mixins import LoginRequiredMixin

urlpatterns = [
    path('', views.BoardList.as_view()),
]
