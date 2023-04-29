from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchListSerializers, StreamPlatformSerializer, ReviewSerializers
# from rest_framework import mixins
from rest_framework import generics

class ReviewCreateView ( generics.CreateAPIView ):
    serializer_class = ReviewSerializers
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get( pk=pk )
        serializer.save( watchlist=movie)


class ReviewList ( generics.ListAPIView ):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter( watchlist = pk )
        
    
class ReviewDetail ( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

    


# class ReviewDetail ( mixins.RetrieveModelMixin, generics.GenericAPIView ):
#     queryset =Review.objects.all()
#     serializer_class = ReviewSerializers
    
#     def retrieve(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
# class ReviewList ( mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView ):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializers
    
#     def get (self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post (self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
        




class StreamPlatformView (APIView):
    
    serializer_class = StreamPlatformSerializer
    
    def get (self, request, *args, **kwargs):
        streaming = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(streaming, many= True, )
        return Response({'message':'successful', 'data':serializer.data}, status=status.HTTP_200_OK)
    
    def post (self, request, *args, **kwargs):
        serializers = StreamPlatformSerializer( data = request.data )
        if serializers.is_valid():
            serializers.save()
            return Response({'message':'success', 'data':serializers.data}, status=status.HTTP_201_CREATED)
        return Response({'message':'failed', 'data':serializers.errors}, status=status.HTTP_400_BAD_REQUEST)


class  StreamPlatformDetailView (APIView):
    serializer_class = StreamPlatformSerializer
    
    def get (self, request, pk ):
        try:
            streaming = StreamPlatform.objects.get( pk=pk )
        except StreamPlatform.DoesNotExist:
            
            return Response({"message":" Not found"},status.HTTP_404_NOT_FOUND)
            
        serializers = StreamPlatformSerializer( streaming )
        return Response(serializers.data, status = status.HTTP_302_FOUND )
    
    def put ( self, request, pk):
        streaming = StreamPlatform.objects.get( pk=pk )
        serializers = StreamPlatformSerializer( streaming, data = request.data )
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_202_ACCEPTED )
        else:
            return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
        
        
    def delete( self, request, pk ):
        streaming = StreamPlatform.objects.get(pk = pk)
        streaming.delete()
        return Response({ 'status':'item deleted'}, status = status.HTTP_204_NO_CONTENT )
        





class WatchListView(APIView):
    
    serializer_class = WatchListSerializers
    
    def post (self, request, *args, **kwargs):
        serializer = WatchListSerializers( data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED )
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST )

    def get ( self, request ):
        
        qs = WatchList.objects.all()
        serializer = WatchListSerializers( qs, many = True )
        return Response(serializer.data)


class WatchListDetailView(APIView):
    def get ( self, request, pk ):
        try:
            watchlists = WatchList.objects.get( pk=pk )
        except WatchList.DoesNotExist:
            
            return Response({"message":" Not found"},status.HTTP_404_NOT_FOUND)
            
        serializers = WatchListSerializers( watchlists )
        return Response(serializers.data, status = status.HTTP_302_FOUND )
    
    def put ( self, request, pk):
        watchlists = WatchList.objects.get( pk=pk )
        serializers = WatchListSerializers( watchlists, data = request.data )
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_202_ACCEPTED )
        else:
            return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
        
        
    def delete( self, request, pk ):
        watchlists = WatchList.objects.get(pk = pk)
        watchlists.deleete()
        return Response({ 'status':'item deleted'}, status = status.HTTP_204_NO_CONTENT )





# @api_view(['GET', 'POST'])
# def movie_list ( request ):
    
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializers = MovieSerializers( movies, many=True )
#         return Response(serializers.data, status = status.HTTP_200_OK )
    
#     if request.method == 'POST':
#         serializers = MovieSerializers( data = request.data )
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status = status.HTTP_201_CREATED )
#         else:
#             return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST )
            
    



# @api_view(['GET', 'PUT', 'DELETE'])
# def movies_dettail ( request, pk ):
#     if request.method == 'GET':
#         try:
#             movies = Movie.objects.get( pk=pk )
#         except Movie.DoesNotExist:
            
#             return Response({"message":"Movie not found"},status.HTTP_404_NOT_FOUND)
            
#         serializers = MovieSerializers( movies )
#         return Response(serializers.data, status = status.HTTP_302_FOUND )

#     if request.method == 'PUT':
#         movies = Movie.objects.get( pk=pk )
#         serializers = MovieSerializers( movies, data = request.data )
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status = status.HTTP_202_ACCEPTED )
#         else:
#             return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE':
#         movies = Movie.objects.get( pk=pk )
#         movies.delete()
#         return Response({ 'status':'item deleted'}, status = status.HTTP_204_NO_CONTENT )