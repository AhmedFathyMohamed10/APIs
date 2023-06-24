from django.db import models
import uuid

class Guest(models.Model):
    user_id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11)

    def __str__(self) -> str:
        return f'{self.name}'
    
class Movie(models.Model):
    title = models.CharField(max_length=200)
    ratings = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self) -> str:
        return self.title
    
class Reservation(models.Model):
    guest = models.ForeignKey(Guest, related_name='reservation', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reservation', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Name: {self.guest} Reserved a: {self.movie}'
