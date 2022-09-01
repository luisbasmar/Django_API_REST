import json
from django.views import View
from .models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import requests
# Create your views here.

def get_users():

        url = 'https://jsonplaceholder.typicode.com/users'
        response = requests.get(url)
        users = response.json()
        
        for i in users:
            User.objects.get_or_create(
                name = i['name'],
                user_name = i['username'],
                email = i['email'],
            )

class UserView(View):


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        get_users()
        if id > 0:
            users = list(User.objects.filter(id=id).values())
            if len(users) > 0:
                user = users[0]
                datos={'message':"success", 'user': user}
            else:
                datos={'message':  'user not found'}
            return JsonResponse(datos)
        else:
            users = list(User.objects.values())
            if len(users) > 0:
                datos={'message':"success", 'users': users}
            else:
                datos={'message':  'users not found'}
            return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        User.objects.create(name=jd['name'], user_name=jd['user_name'], email=jd['email'])
        datos={'message':"success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        users = list(User.objects.filter(id=id).values())
        if len(users) > 0:
            user = User.objects.get(id=id)
            user.name =jd["name"]
            user.user_name =jd["user_name"]
            user.email =jd["email"]
            user.save()
            datos={'message':"success"}
        else:
            datos={'message':  'user not found'}
        return JsonResponse(datos)
        
    def delete(self, request, id):
        users = list(User.objects.filter(id=id).values())
        if len(users) > 0:
            User.objects.filter(id=id).delete()
            datos={'message':"success"}
        else:
            datos={'message':  'user not found'}
        return JsonResponse(datos)



# def users(request):
#     #pull data from third party rest api
#     response = requests.get('https://jsonplaceholder.typicode.com/users')
#     #convert reponse data into json
#     users = response.json()
#     print(users)
#     return HttpResponse(response)