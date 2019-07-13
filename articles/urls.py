from django.urls import path
from . import views


app_name = "articles"

urlpatterns = [
    path('', views.article_list, name="list"),
    path('create/', views.article_create, name="create"),
    path('delete/(?P[0-9]+)', views.article_delete, name='delete'),
    path('<slug>/', views.article_detail, name="detail"),
]