from django.urls import path 
from .views import home , create , show_post , update , delete


urlpatterns = [
    path('', home , name="home"),
    path('create', create , name="create"),
    path('show/<int:pk>/', show_post , name="show_post"),
    path('post/<int:pk>/update/', update , name="update"),
    path('post/<int:pk>/delete/', delete , name="delete"),
]