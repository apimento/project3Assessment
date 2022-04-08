from django.urls import path
from django.urls import URLPattern 
from . import views   

urlpatterns = [ 
    path('', views.home, name='home') ,
    path('widgets/add_widget', views.add_widget, name="add_widget") ,
    path("widgets/<int:pk>/delete/", views.WidgetDelete.as_view(), name="delete_widget"),
]