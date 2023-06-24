from django.urls import path
from .views import *

urlpatterns = [
	path('home/', index, name="index"),
    
	#apis
	path('staticjson/', static_json_api),
    path('second_method/', second_method),
    path('get_post_api/', get_post_serializer)
]