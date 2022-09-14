from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    prepopulated_fields = {
        'slug': ('title',)
    }

@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'file')


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'level')
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'rating')


@admin.register(models.SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon', 'url')


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'message')


@admin.register(models.Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'bio')


@admin.register(models.Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)
