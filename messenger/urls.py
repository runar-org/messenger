from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send', views.send, name='send'),
    path('encrypted', views.encrypted, name='encrypted'),
    path('receive', views.receive, name='receive'),
    path('receive/<slug:encryption_id>', views.receive, name='receive'),
    path('result', views.result, name='result'),
]