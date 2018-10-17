from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('',views.ListGroups.as_view(), name='all'),
    path('new/',views.CreateGroup.as_view(), name='create'),
    path('post/in/(?P<slug>[-/w]+)/',views.SingleGroup.as_view(), name='all'),
    
]