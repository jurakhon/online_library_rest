from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from django_filters import rest_framework as filters

# Create your views here.

class GenreListAPIView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name',]
    ordering_fields = ['name',]

class GenreCreateAPIView(CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PublisherListAPIView(ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name','address']
    ordering_fields = ['name','address']

class PublisherCreateAPIView(CreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name','surname','address']
    ordering_fields = ['name','surname','address']
    search_fields = ['name','surname']


class AuthorCreateAPIView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['title', 'author', 'publisher', 'genres', 'quantity','publication_date']
    ordering_fields = ['title', 'author', 'publisher', 'genres', 'quantity','publication_date']

class BookListAPIView2(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        title = self.request.query_params.get('title', None)
        author = self.request.query_params.get('author', None)

        if author:
            queryset = queryset.filter(author__name__icontains=author)
        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset


class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['title', 'author', 'publisher', 'genres', 'quantity','publication_date']
    ordering_fields = ['title', 'author', 'publisher', 'genres', 'quantity','publication_date']


class BorrowListAPIView(ListAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['user', 'book', 'borrowed_date', 'return_date']
    ordering_fields = ['user', 'book', 'borrowed_date', 'return_date']

class BorrowCreateAPIView(CreateAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer


