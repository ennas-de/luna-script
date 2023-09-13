from django.urls import path

from .views import (
    PostListAPIView,
    SinglePostAPIView,
    TagAPIView,
    TagListView,
)

urlpatterns = [

    # Posts

    path('list-view/', PostListAPIView.as_view(), name='list_view'),
    path('<str:slug>/detail-view/', SinglePostAPIView.as_view(), name='detail_view'),

    # Tags

    path('tags/lists/', TagListView.as_view(), name='tags_list'),
    path('tags/<str:slug>/', TagAPIView.as_view(), name='tags_filter'),
]