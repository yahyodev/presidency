from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from . import models, serializers


class CacheMixin:
    @method_decorator(cache_page(60 * 60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class LessonListView(ListAPIView, CacheMixin):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer


class LessonDetailView(RetrieveAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer
    lookup_field = 'slug'


class PostListView(ListAPIView, CacheMixin):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetailView(RetrieveAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    lookup_field = 'slug'


class ReviewListView(ListAPIView, CacheMixin):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class SocialAccountListView(ListAPIView, CacheMixin):
    queryset = models.SocialAccount.objects.all()
    serializer_class = serializers.SocialAccountSerializer


class ContactView(CreateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class HomeView(APIView):
    @method_decorator(cache_page(60 * 60 * 1))
    def get(self, request, *args, **kwargs):
        return Response(serializers.HomeSerializer(models.Home.get_solo()).data)


class SubscriptionView(CreateAPIView):
    queryset = models.Subscription.objects.all()
    serializer_class = serializers.SubscriptionSerializer
