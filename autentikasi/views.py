

# Create your views here.
import json
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import redirect

from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def signup(request):
    if request.method == 'POST':
        deserialize = json.loads(request.body)
        username = deserialize['username']
        password = deserialize['password']
        email = deserialize['email']
        print(username,password,email)
        user = User.objects.create_user(email=email,username=username,password=password)
        user.save()

        return JsonResponse({
            "message": "Account created"
        })  


@csrf_exempt
def login_user(request):

    if request.method == 'POST':
        deserialize = json.loads(request.body)
        username = deserialize['username']
        password = deserialize['password']
        print(username,password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            # redirect ke home
            return JsonResponse({'success': True, 'user_id':user.id, 'user_name':user.username})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})


@csrf_exempt
def logout_user(request):
    if request.method == 'POST':
        del request.session['user_id']
        logout(request)
        return JsonResponse({
            "message": "logout berhasil"
        })  

def get_username(request):
    if request.user.is_authenticated:
        username = request.user.username
        return JsonResponse({'username': username})
    else:
        return JsonResponse({'error': 'User is not authenticated'})
    
def get_session_id(request):
    session_id = request.session.session_key
    user_id = request.session.get('user_id')
    data = {'session_id': session_id, 'user_id': user_id}
    return JsonResponse(data)