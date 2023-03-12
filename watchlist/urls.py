from django.urls import path

from .views import watchList,createwatchList,deletewatchList
urlpatterns = [
    path('', watchList, name='watch-list'),
    path('create/', createwatchList, name='createwatch-list'),
    path('delete/', deletewatchList, name='deletewatch-list')
]