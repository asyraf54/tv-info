from django.urls import path

from .views import show_list,show_detail
urlpatterns = [
    path('', show_list, name='show-list'),
    path('<int:pk>/', show_detail, name='show-detail'),
]