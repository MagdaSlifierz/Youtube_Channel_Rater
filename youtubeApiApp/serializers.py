from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import YoutubeChannel, Rating
from django.contrib.auth.models import User

class YoutubeChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeChannel
        fields = ('id', 'title', 'description', 'number_of_ratings', 'avarage_rating')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'user', 'youtube', 'stars')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password') #hash the password so user can not see that on url
        extra_kwargs = {'password':{'write_only':True, 'required':True}} #adding more info to password I can only write, no save it and requierd if register

    def create(self, validated_data): #data comming from request
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
