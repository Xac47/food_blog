from django.urls import path

from contact import views

urlpatterns = [
    path('', views.GetInTouchView.as_view(), name='contact'),
    path('subscribe_email/', views.SubscribeEmailView.as_view(), name='subscribe-email')
]