from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from app.models.user import User
from app.serializers.user import UserSerializer
from app.validators.user import isPositiveNumber
from django.core.exceptions import ValidationError


@api_view(['GET'])
def eventList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def show(request, id):
    user = User.objects.get(id=id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def deposit(request, id):
  user = User.objects.get(id=id)
  amount = request.data.get('amount')
  if not isPositiveNumber(amount): return Response("Please enter a valid Positive Number", status = 422)

  serializer = UserSerializer(user, many=False)
  user.wallet+= int(amount)
  user.save()
  return Response(serializer.data)


@api_view(['POST'])
def withdraw(request, id):
  user = User.objects.get(id=id)
  amount = request.data.get('amount')
  if not isPositiveNumber(amount): return Response("Please enter a valid Positive Number", status = 422)

  serializer = UserSerializer(user, many=False)
  user.wallet-= int(amount)
  user.full_clean()
  user.save()
  return Response(serializer.data)

