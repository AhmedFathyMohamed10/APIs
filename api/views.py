from django.shortcuts import render
from django.http.response import JsonResponse
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *

def index(request):
	return render(request, 'index.html')

def static_json_api(request):
	guests = [
		{
			'id': 1,
			'name': 'Ahmed',
			'mobile': '01019281921'
		},
		{
			'id': 2,
			'name': 'Mohamed',
			'mobile': '1018192881'
		},
		{
			'id': 3,
			'name': 'Israa',
			'mobile': '9182881911'
		}
	]

	return JsonResponse(guests, safe=False) # safe is false: data isn't hashable.


def second_method(request):

	guests = Guest.objects.all()
	print(guests.values())
	response = {
		"data": list(guests.values('name', 'mobile'))
	}
	return JsonResponse(response)


@api_view(['GET', 'POST'])
def get_post_serializer(request):
	if request.method == 'GET':
		guests = Guest.objects.all()
		serializer = GuestSerializer(guests, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	
	elif request.method == 'POST':
		data = request.data
		serializer = GuestSerializer(data=data)

		if serializer.is_valid(): # to make sure that the data is valid.
			serializer.save()  # save to database
			return Response(serializer.data, status=status.HTTP_201_CREATED)

