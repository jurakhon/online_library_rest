from django.urls import path
from .views import *

urlpatterns = [
    path('booklist/', BookListAPIView.as_view(), name='booklist'),
    path('booklist2/', BookListAPIView2.as_view(), name='booklist2'),
    path('bookcreate/', BookCreateAPIView.as_view(), name='bookcreate'),
    path('borrowlist/', BorrowListAPIView.as_view(), name='borrowlist'),
    path('genrelist/', GenreListAPIView.as_view(), name='genrelist'),
    path('genrecreate/', GenreCreateAPIView.as_view(), name='genrecreate'),
    path('publisherlist/', PublisherListAPIView.as_view(), name='publisherlist'),
    path('publishercreate/', PublisherCreateAPIView.as_view(), name='publishercreate'),
    path('authorlist/', AuthorListAPIView.as_view(), name='authorlist'),
    path('authorcreate/', AuthorCreateAPIView.as_view(), name='authorcreate'),
    path('borrowcreate/', BorrowCreateAPIView.as_view(), name='borrowcreate'),




]