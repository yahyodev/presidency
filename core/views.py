from django.http import JsonResponse
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
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


class HomeView(APIView):
    def get(self, request, *args, **kwargs):
        data = models.Home.get_solo()
        return Response(serializers.HomeSerializer(data).data)


class SubscriptionView(CreateAPIView):
    queryset = models.Subscription.objects.all()
    serializer_class = serializers.SubscriptionSerializer


class TypeListView(ListAPIView):
    serializer_class = serializers.TypeSerializer

    def get_queryset(self):
        parents = []
        for i in models.Type.objects.all():
            if i.parent is None:
                parents.append(i)

        return parents
