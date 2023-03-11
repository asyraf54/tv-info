import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from watchlist.models import WatchList
from rest_framework import status
from django.contrib.auth.models import User
from myList.models import Show

# Create your views here.
@csrf_exempt
def watchList(request):
    if request.method == 'POST':
        deserialize = json.loads(request.body)
        user_id = deserialize.get('user')
        shows = Show.objects.filter(watchlist__user_id=user_id)
        show_list = []
        for show_obj in shows:
            show_dict = {
                'id':  show_obj.id,
                'title': show_obj.title,
                'synopsis': show_obj.synopsis,
                'time_publish': show_obj.time_publish,
                'genre': show_obj.genre,
                'poster_url': show_obj.poster_url,
                'trailer_url': show_obj.trailer_url,
            }
            show_list.append(show_dict)
        data = {'watch_lists': show_list}
        return JsonResponse(data)
    
@csrf_exempt
def createwatchList(request):    
    if request.method == 'POST':
        deserialize = json.loads(request.body)
        user = User.objects.get(id=deserialize['user'])
        show = Show.objects.get(id=deserialize['show'])
        watch_list = WatchList(user = user ,show=show)
        watch_list.save()
        return JsonResponse({'message': 'watch list created successfully'}, status=status.HTTP_201_CREATED)

@csrf_exempt
def deletewatchList(request):
    if request.method == 'DELETE':
        deserialize = json.loads(request.body)
        user = User.objects.get(id=deserialize['user'])
        show = Show.objects.get(id=deserialize['show'])
        print(user,show)
        item = WatchList.objects.filter(user=user, show=show)
        item.delete()
        return JsonResponse({'success': 'Item deleted from watchlist'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
       