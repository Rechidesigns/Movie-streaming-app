
from django.urls import path, include
from watchlist_app.api.views import (WatchListView, WatchListDetailView, StreamPlatformView,
                                     StreamPlatformDetailView, ReviewDetail, ReviewList, 
                                     ReviewCreateView )


urlpatterns = [
    path('watchlist/', WatchListView.as_view(), name = 'add-movie'),
    path('watchlist/<int:pk>', WatchListDetailView.as_view(), name = 'Movies-detail'),
    path('stream/', StreamPlatformView.as_view(), name = 'add-streaming-platform'),
    path('stream/<int:pk>', StreamPlatformDetailView.as_view(), name = 'streaming-detail'),
    
    # path('review/', ReviewList.as_view(), name = 'review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name = 'review-detail'),

    path('stream/<int:pk>/review-create', ReviewCreateView.as_view(), name = 'review-create'), 
    path('stream/<int:pk>/review', ReviewList.as_view(), name = 'review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name = 'review-detail'),
]