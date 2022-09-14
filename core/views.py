from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from . import models, serializers


class LessonListView(ListAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer


class PostListView(ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class ReviewListView(ListAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class SocialAccountListView(ListAPIView):
    queryset = models.SocialAccount.objects.all()
    serializer_class = serializers.SocialAccountSerializer


class ContactView(ListAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer

    def get_queryset(self):
        return models.Contact.objects.first() or models.Contact.objects.none()


class HomeView(ListAPIView):
    queryset = models.Home.objects.all()
    serializer_class = serializers.HomeSerializer

    def get_queryset(self):
        return models.Home.objects.first() or models.Contact.objects.none()


class SubscriptionView(CreateAPIView):
    queryset = models.Subscription.objects.all()
    serializer_class = serializers.SubscriptionSerializer
