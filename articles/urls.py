from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('<slug>/', views.article_detail),
]