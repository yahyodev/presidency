from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers
from django.core.cache import cache


class LessonListView(ListAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer


class LessonDetailView(RetrieveAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer
    lookup_field = 'slug'


class PostListView(ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetailView(RetrieveAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    lookup_field = 'slug'


class ReviewListView(ListAPIView):
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        return cache.get_or_set('review', models.Review.objects.all(), 3000)


class SocialAccountListView(ListAPIView):
    serializer_class = serializers.SocialAccountSerializer

    def get_queryset(self):
        return cache.get_or_set('SocialAccount', models.SocialAccount.objects.all(), 3000)

class ContactView(CreateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class HomeView(APIView):
    def get(self, request, *args, **kwargs):
        data = cache.get_or_set('Home', models.Home.get_solo(), 3000)
        return Response(serializers.HomeSerializer(data).data)


class SubscriptionView(CreateAPIView):
    queryset = models.Subscription.objects.all()
    serializer_class = serializers.SubscriptionSerializer
