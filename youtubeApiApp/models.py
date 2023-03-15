from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class YoutubeChannel(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=360)

    def number_of_ratings(self):
        ratings = Rating.objects.filter(youtube=self)
        return len(ratings)
    
    def avarage_rating(self):
        ratings = Rating.objects.filter(youtube=self)
        sum = 0
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            avarage = sum / len(ratings)
        else:
            return 0
        return avarage


class Rating(models.Model):
    youtube = models.ForeignKey(YoutubeChannel, on_delete=models.CASCADE) #if remove model YCh then remove the rating 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #use validators to make sure user click only on 1-5 starts
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        #if I already have rated it with specific user, next time will be rejected. Only one user - one ratign for channel
        unique_together = (('user', 'youtube'))
        index_together = (('user', 'youtube'))