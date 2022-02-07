from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('veterinaryoffices/', views.veterinaryoffices, name='veterinaryoffices'),
    path('shelters/', views.shelters, name='shelters'),
    path('shelters/<int:shelter_id>', views.shelter_by_id, name='shelter_by_id')
]