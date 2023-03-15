
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import YoutubeChannelSerializer, RatingSerializer, UserSerializer

from django.shortcuts import render
from django.contrib.auth.models import User
from .models import YoutubeChannel, Rating

# Create your views here.

class YoutubeChannelViewSet(viewsets.ModelViewSet):
    queryset = YoutubeChannel.objects.all()
    serializer_class = (YoutubeChannelSerializer) 
    authentication_classes = (TokenAuthentication , )
    permission_classes = (IsAuthenticated, )

    @action(detail=True, methods=['POST'] ) #decorate method with values detailTrue specific movie
    def rate_youtube_channel(self, request, pk=None):
        #get data for rating
        if 'stars' in request.data:
            #get select from database specific objects
            channel = YoutubeChannel.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user # this is used from TokenAuthentication
            # user = User.objects.get(id=1)
            
            #check if rating already exists
            try:
                #if rating already exist get it and update it 
                rating = Rating.objects.get(user=user.id, youtube=channel.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating) #serialize your data
                response = {'message': 'You updated your rating for',
                            'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                #if rating does not exist create one
                rating = Rating.objects.create(user=user, youtube=channel, stars=stars)
                serializer = RatingSerializer(rating) #serialize your data
                response = {'message': 'You created your rating',
                            'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You forget to rate it. Please provide your rating!'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class RatingsViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = (RatingSerializer)
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

      
    def update(self, request, *args, **kwargs):
        response = {'message': 'Its not allowd to update your rating'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'Its not allowd to create your rating'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = (UserSerializer) 
    
