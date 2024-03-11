from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='blog'),
    path('blog/details/<int:id>', views.details, name='details'),
    path('blog/details/<int:id>', views.details, name='details'),

]