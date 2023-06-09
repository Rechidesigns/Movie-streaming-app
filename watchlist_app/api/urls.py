
from django.urls import path, include
from watchlist_app.api.views import (WatchListView, WatchListDetailView, StreamPlatformView,
                                     StreamPlatformDetailView, ReviewDetail, ReviewList, 
                                     ReviewCreateView, UserReview, WatchList2 )


urlpatterns = [
    path('watchlist/', WatchListView.as_view(), name = 'add-movie'),
    path('watchlist/<int:pk>/', WatchListDetailView.as_view(), name = 'Movies-detail'),
    path('stream/', StreamPlatformView.as_view(), name = 'add-streaming-platform'),
    path('stream/<int:pk>/', StreamPlatformDetailView.as_view(), name = 'streaming-detail'),
    
    
    path('watchlist2/', WatchList2.as_view(), name = 'watchlist2-detail'),
    
    # path('review/', ReviewList.as_view(), name = 'review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name = 'review-detail'),

    path('<int:pk>/review-create/', ReviewCreateView.as_view(), name = 'review-create'), 
    path('<int:pk>/reviews/', ReviewList.as_view(), name = 'review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name = 'review-detail'),
    
    
    # path('review/<str:username>/', UserReview.as_view(), name = 'user-review-detail'),
    path('review/', UserReview.as_view(), name = 'user-review-detail'),
    
    
    # path('<int:pk>/review-create/', ReviewCreateView.as_view(), name='review-create'),
    # path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    # path('reviews/', UserReview.as_view(), name='user-review-detail'),

]

