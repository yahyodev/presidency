from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from . import models, serializers


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
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class SocialAccountListView(ListAPIView):
    queryset = models.SocialAccount.objects.all()
    serializer_class = serializers.SocialAccountSerializer


class ContactView(CreateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class HomeView(ListAPIView):
    queryset = models.Home.objects.all()
    serializer_class = serializers.HomeSerializer

    def get_queryset(self):
        return models.Home.objects.first() or models.Home.objects.none()


class SubscriptionView(CreateAPIView):
    queryset = models.Subscription.objects.all()
    serializer_class = serializers.SubscriptionSerializer
