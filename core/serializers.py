from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from . import models


class LessonSerializer(ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = '__all__'


class PostSerializer(ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'


class SocialAccountSerializer(ModelSerializer):
    class Meta:
        model = models.SocialAccount
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    class Meta:
        model = models.Contact
        fields = '__all__'


class HomeSerializer(ModelSerializer):
    class Meta:
        model = models.Home
        fields = '__all__'


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = models.Subscription
        fields = '__all__'


class TypeChildSerializer(ModelSerializer):
    class Meta:
        model = models.Type
        fields = ('title', 'slug', 'order',)


class TypeSerializer(ModelSerializer):
    children = SerializerMethodField()

    class Meta:
        model = models.Type
        fields = ('title', 'slug', 'order', 'children')

    def get_children(self, obj):
        children = []
        for i in models.Type.objects.all():
            if i.parent and i.parent.id == obj.id:
                children.append(i)

        return TypeChildSerializer(children, many=True).data
