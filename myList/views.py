import json
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Show
from django.core import serializers
from rest_framework import serializers

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = '__all__'

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
        return JsonResponse({'message': 'Group created successfully'}, status=status.HTTP_201_CREATED)
    

@csrf_exempt
def show_detail(request, pk):
    show = get_object_or_404(Show, pk=pk)
    if request.method == 'GET':
        serializer = ShowSerializer(show)
        return JsonResponse(serializer.data)
    
    elif request.method == 'DELETE':
        show.delete()
        data = {'message': 'Post deleted successfully!'}
        return JsonResponse(data)