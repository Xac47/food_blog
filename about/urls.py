from django.urls import path

from about import views

urlpatterns = [
    path('', views.AboutView.as_view(), name='about')
]