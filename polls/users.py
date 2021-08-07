from django.http import JsonResponse
from polls.models import User
from polls.serializers import UserSerializer
import json


def userView(request):
  json_data = json.loads(request.body)
  user_id = json_data.get('user_id')
  user = User.objects.filter(id=user_id).first()
  if not user: 
    return JsonResponse('User not found', safe = False, status= 404)

  return JsonResponse(UserSerializer(user), safe=False)

def deposit(request):
  json_data = json.loads(request.body)
  user_id = json_data.get('user_id')
  user = User.objects.filter(id=user_id).first()
  if not user:  return JsonResponse('User not found', safe = False, status= 404)
  if not json_data['amount']:  return JsonResponse('Please enter a valid data', safe = False, status= 404)
  user.wallet+= json_data['amount']
  user.save()
  return JsonResponse(UserSerializer(user), safe=False)

def withdraw(request):
  json_data = json.loads(request.body)
  user_id = json_data.get('user_id')
  user = User.objects.filter(id=user_id).first()
  if not user: return JsonResponse('User not found', safe = False, status= 404)

  if not json_data['amount']: return JsonResponse('Please enter a valid data', safe = False, status= 404)
  user.wallet-= json_data['amount']
  user.save()
  return JsonResponse(UserSerializer(user), safe=False)


  