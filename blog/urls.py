from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('category/<slug:slug>/', views.CategoryListView.as_view(), name='category-posts'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post'),
]
