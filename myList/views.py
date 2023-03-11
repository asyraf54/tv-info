import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Show

@csrf_exempt
def show_list(request):
    if request.method == 'GET':
        shows = Show.objects.all()
        data = {'shows': list(shows.values())}
        return JsonResponse(data)
    elif request.method == 'POST':
        deserialize = json.loads(request.body)
        show = Show(title=deserialize['title'],synopsis=deserialize['synopsis'], time_publish=deserialize['time_publish'],
                    genre=deserialize['genre'],poster_url=deserialize['poster_url'], trailer_url=deserialize['trailer_url'])
        show.save()
        return JsonResponse(show)

@csrf_exempt
def show_detail(request, pk):
    show = get_object_or_404(Show, pk=pk)
    if request.method == 'GET':
        return JsonResponse(show)
    elif request.method == 'PUT':
        deserialize = json.loads(request.body)
        show = Show(title=deserialize['title'],synopsis=deserialize['synopsis'], time_publish=deserialize['time_publish'],
                    genre=deserialize['genre'],poster_url=deserialize['poster_url'], trailer_url=deserialize['trailer_url'])
        show.save()

        return JsonResponse(show)
    elif request.method == 'DELETE':
        show.delete()
        data = {'message': 'Post deleted successfully!'}
        return JsonResponse(data)