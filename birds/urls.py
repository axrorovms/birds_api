from django.urls import path
from birds import views


app_name = 'birds'
urlpatterns = [
    path('bird-create', views.BirdsCreateApiView.as_view(),  name='bird_create'),
    path('bird-list', views.BirdsListApiView.as_view(),  name='bird_list'),
    path('bird-detail/<int:id>', views.BirdsDetailAPIView.as_view(),  name='bird_list'),
]