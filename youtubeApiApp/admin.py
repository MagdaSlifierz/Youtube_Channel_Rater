from django.contrib import admin

from .models import YoutubeChannel, Rating
# Register your models here.

admin.site.register(YoutubeChannel)
admin.site.register(Rating)