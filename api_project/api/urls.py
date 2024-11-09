from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView, name='api-overview'),
    path('language-list/', views.languageList, name='language-list'),
    path('language-detail/<str:pk>/', views.languageDetail, name='language-detail'),
    path('language-create/', views.languageCreate, name='language-create'),
    path('language-update/<str:pk>/', views.languageUpdate, name='language-update'),
    path('language-delete/<str:pk>/', views.languageDelete, name='language-delete')
]
