from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializers ( serializers.ModelSerializer ):
    
    user_review = serializers.StringRelatedField(read_only = True)
    
    class Meta:
        model = Review
        exclude = [ 'watchlist' ]
        # fields = "__all__"

class WatchListSerializers ( serializers.ModelSerializer ):
    
    # movie_reviews = ReviewSerializers( many= True, read_only = True )
    platform = serializers.CharField( source = 'platform.name')
    
    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer ( serializers.ModelSerializer ):
    
    Watchlist =  WatchListSerializers ( many=True, read_only=True )
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"







# def name_lenght(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name must be at least 2 characters longer")
    
    
# class MovieSerializers ( serializers.Serializer):
#     id = serializers.IntegerField( read_only=True)
#     name = serializers.CharField(validators = [name_lenght])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError( 'name and description can not be the same')
#         else:
#             return data
    
    # def validate_name (self, value ):
    #     if len(value) < 3:
    #         raise serializers.ValidationError(" Name must be at least 3 characters longer")
    #     else:
    #         return value
    